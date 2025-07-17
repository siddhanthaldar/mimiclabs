# Task Suites


You can create your own suite of tasks in MimicLabs by cerating a path under `mimiclabs/mimiclabs/task_suites`. Each task suite can contain multiple tasks each represented by a BDDL file. We use the BDDL infrastructure setup by LIBERO and extend it to include the ability to specify camera poses, textures, and demonstration states for MimicGen.

Below we discuss all the critical components that make up a task config in BDDL. An example task suite is available in `mimiclabs/mimiclabs/task_suites/example_suite`.

## Create your own task

### Scene
The first thing to provide in a task BDDL is the scene for your task. Same as LIBERO, we define each scene as a `problem` in the BDDL, which contains the specs for the scene background, the table geometry, and the robot positioning with respect to the table.

Below is an example showing problem specification in a BDDL:
```
(problem MimicLabs_Lab1_Tabletop_Manipulation)
```

MimicLabs contains 8 such problem classes, using which we can instantiate tasks in 8 different virtual "labs". You can find these problem classes in `mimiclabs/env/problems/mimiclabs_tabletop_manipulation.py`.

### Object placement regions
After specyfing the scene, next you will need to define initialization regions that will later be used for stating state initialization, goal, and demonstration predicates. We borrow many conventions from LIBERO to specify initialization regions of objects relative to a target table, as well as regions within fixtures.

Below is an example region named `object_init_region`:
```
(object_init_region
    (:target table)
    (:ranges (
        (-0.2 -0.1 0 0.1)
      )
    )
    (:yaw_rotation (
        (0.0 0.0)
      )
    )
)
```

`:target` specifies what entity this region is relative to. The target `table` here is a keyword that anchors the provided range onto the appropriate table. All scenes in MimicLabs contain the same table geometry for simplicity, and all scenes contain just one table. Hence you can just use `table` as the target for objects in all MimicLabs scenes.

`:ranges` is a list of (x, y) ranges, where each range is specified as a 4-tuple (x_start y_start x_end y_end).

`:yaw_rotation` is specified as a range in radians, for each range. Note that the yaw rotation provided in the object class takes precedence as does not override it.


### Camera poses

You may provide the initialization distribution of the `agentview` camera pose in the task config. 

Below is an example of how a camera initialization specification comes together in a BDDL, between distances 1.2m to 1.4m from the center of the table, pitch ranging from 45 to 60 degrees, yaw ranging from -15 to 15 degrees.
```
(:camera
  (:ranges (
      (1.2 45 -15 1.4 60 15)
    )
  )
  (:jitter_mode normal)
  (:unit degrees)
)
```

`:ranges` is provided as a list of 6-tuple(s) of floating-point numbers. First three are the initial `r`, `theta`, `phi` values in [spherical coordinates](https://en.wikipedia.org/wiki/Spherical_coordinate_system) (physics convention), and the last three the final values. This creates a region for perturbance of the camera at each scene initialization. By default, `r` is in metres, `theta` and `phi` are in radians (can optionally be specified in degrees, see below for setting the unit for angles). The camera always points at the center of the table. 

`:jitter_mode` specifies how the camera jitters within each provided range. Current supported modes are `uniform` (uniform sampling in the provided range) and `normal` (normal distribution with mean at the center of the provided range with ~98% of the samples falling within the provided range).

`:unit` (optional) lets you set the unit to `degrees` if you want to specify `theta` and `phi` in degrees instead of the default unit `radians`.


### Machine-generated textures for objects and table

You may provide specs for generating a new texture at each environment initialization. 

Below is an example that shows how you can use the `fractal` algorithm to generate textures for an object (named `object_1` here) on the fly, and the `jitter` algorithm to randomly jitter the color of the table (named `table` in the scene/problem) at each task initialization:
```
(:textures
  (object_1
    (:type fractal)
    (:hsv (
        (50 150 150 70 255 255)
        (110 150 150 130 255 255)
      )
    )
    (:turbulence 2)
    (:sigma 5)
  )
  (table
    (:type jitter)
    (:hsv (
        (170 150 150 179 255 255)
        (0 150 150 10 255 255)
        (50 150 150 59 255 255)
        (60 150 150 70 255 255)
        (110 150 150 119 255 255)
        (120 150 150 130 255 255)
      )
    )
  )
)
```

`:type` specifies the algorithm used to generate the texture. Supported types are `fractal` and `jitter`. Both `fractal` and `jitter` algorithms accept `:hsv` ranges, whereas the `fractal` algorithm accepts additional `:turbulence` and `:sigma` values.


By default, textures are generated and stored in the path `<path_to_this_repo>/mimiclabs/tmp`. However, you can specify your own path by setting the `MIMICLABS_TMP_FOLDER` environment variable as:
```bash
$ export MIMICLABS_TMP_FOLDER=/my/custom/tmp/folder
```
<!-- add examples from paper appendix -->


### Task initialization

Having specified objects and different initialization regions, we can now specify predicates for initializing the scene. Below is an example:
```
(:init
  (On object_1 table_object_init_region)
  (On wooden_cabinet_1 table_wooden_cabinet_init_region)
  (Open wooden_cabinet_1_top_region)
)
```

Each predicate starts with an operator followed by 1 or 2 operands. Each operand is either an object/fixture/site identifier (e.g. `object_1`, `wooden_cabinet_1`, `wooden_cabinet_1_top_region` respectively), or a region. Each region is specified as `<target_name>_<region_name>`.

### Task goal
The goal for your task should be provided as a predicate or multiple predicates connected with an `And` or `Or` operator.

Example of a single-goal specification in BDDL:
```
(:goal
    (In object_1 wooden_cabinet_1_top_region)
)
```
Examples of multi-goal specification in BDDL:
```
(:goal
    (And (Open wooden_cabinet_1_top_region) (In object_1 wooden_cabinet_1_top_region))
)
```
```
(:goal
    (Or (Open wooden_cabinet_1_top_region) (In object_1 wooden_cabinet_1_top_region))
)
```
Note that we support goal conjunctions using both `And` and `Or` predicates. This enables the task goal to be multi-modal.


### Demonstration subtasks

We need to specify subtask demonstration predicates to help MimicGen understand how the demonstrations are collected for this task. We use these predicates to split the provided demonstration into **object-centric** chunks, and use MimicGen to expand the demonstration set by warping trajectories around the target object for each subtask chunk.

For example: if the task is to ``open the drawer and put the bowl in it``, you may provide the following subtasks in your BDDL: </br>
> a. open the drawer </br>
> b. grasp the bowl </br>
> c. put the bowl in the drawer </br>

Below is an example specifying the `goal` and `demonstration` states in a task BDDL:
```
(:goal
    (In object_1 wooden_cabinet_1_top_region)
)

(:demonstration
    (Open wooden_cabinet_1_top_region)
    (Grasp object_1)
    (In object_1 wooden_cabinet_1_top_region)
)
```

The demo collection script also uses these predicates to guide data collection predicate by predicate.

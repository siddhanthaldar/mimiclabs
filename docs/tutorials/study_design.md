# Design a study

You can use MimicLabs to design a dataset composition study for your robot policy. In our study paper, we designed `collector` and `retriever` experiments that drew conclusions about how should practitioners collect new datasets as well as use existing large-scale datasets for co-training their downstream policy.

## Collector's Study

We consider collectors as practitioners who are contributing demonstrations to a large robotics dataset. Since data collection is time-consuming, we seek to understand which dimensions of variation (DVs) should be prioritized for diversity or alignment during data collection to facilitate downstream task learning.

### Camera pose

To understand the importance of camera poses in data collection, we setup a target task and co-train it with datasets that have camera poses sampled in small and large distributions that are mis-aligned with the target camera pose. Camera poses in the target task are sampled in the range below:
```
## Camera pose: Shoulder-left / Shoulder-right

(:camera
  (:ranges (
      (1.2 45 120 1.4 60 150)
      (1.2 45 -150 1.4 60 -120)
    )
  )
  (:unit degrees)
  (:jitter_mode normal)
)
```
We create multiple datasets that differ with the target dataset along just one DV, camera pose in this case. Example mis-aligned camera pose distributions are below:
```
## Camera pose: Agent-front

(:camera
  (:ranges (
      (1.2 45 -15 1.4 60 15)
    )
  )
  (:unit degrees)
  (:jitter_mode uniform)
)
```
```
## Camera pose: Agent-front / Agent-left

(:camera
  (:ranges (
      (1.2 45 -15 1.4 60 15)
      (1.2 45 -60 1.4 60 -30)
    )
  )
  (:unit degrees)
  (:jitter_mode uniform)
)
```
```
## Camera pose: Agent-front / Agent-right

(:camera
  (:ranges (
      (1.2 45 -15 1.4 60 15)
      (1.2 45 30 1.4 60 60)
    )
  )
  (:unit degrees)
  (:jitter_mode uniform)
)
```

### Object texture

To understand the importance of object textures in data collection, we setup a target task and co-train it with object textures (same geometry) sampled in small and large distributions that are mis-aligned with the target object texture. Textures for the object `bowl_1` in the target task are sampled in the range below:
```
## Object texture: blue

(:textures
  (bowl_1
    (:type fractal)
    (:hsv (
        (110 150 150 130 255 255)
      )
    )
    (:turbulence 2)
    (:sigma 5)
  )
)
```
We create multiple datasets that differ with the target dataset along just one DV, object texture in this case. Example mis-aligned object texture distributions are below:
```
## Object texture: green (fixed)

(:textures
  (bowl_1
    (:type fractal)
    (:hsv (
        (50 200 200 70 200 200)
      )
    )
    (:turbulence 2)
    (:sigma 5)
  )
)
```
```
## Object texture: green (varied)

(:textures
  (bowl_1
    (:type fractal)
    (:hsv (
        (50 150 150 70 255 255)
      )
    )
    (:turbulence 2)
    (:sigma 5)
  )
)
```
```
## Object texture: red (fixed)

(:textures
  (bowl_1
    (:type fractal)
    (:hsv (
        (0 200 200 0 200 200)
      )
    )
    (:turbulence 2)
    (:sigma 5)
  )
)
```
```
## Object texture: red (varied)

(:textures
  (bowl_1
    (:type fractal)
    (:hsv (
        (170 150 150 179 255 255)
        (0 150 150 10 255 255)
      )
    )
    (:turbulence 2)
    (:sigma 5)
  )
)
```
```
## Object texture: red (fixed) / green (fixed)

(:textures
  (bowl_1
    (:type fractal)
    (:hsv (
        (0 200 200 0 200 200)
        (60 200 200 60 200 200)
      )
    )
    (:turbulence 2)
    (:sigma 5)
  )
)
```
```
## Object texture: red (varied) / green (varied)

(:textures
  (bowl_1
    (:type fractal)
    (:hsv (
        (170 150 150 179 255 255)
        (0 150 150 10 255 255)
        (50 150 150 59 255 255)
        (60 150 150 70 255 255)
      )
    )
    (:turbulence 2)
    (:sigma 5)
  )
)
```

<div class="admonition warning">
    <p class="admonition-title">Warning: No comments in BDDL</p>
    If you choose to use any of the distributions above, make sure to remove comment marked with ##. 
</div>


## Retriever's Study

A data retriever is a practitioner that seeks to use a pre-existing large-scale dataset with high variation in several DVs (such as DROID) for their specific task of interest. In this setting, we aim to retrieve a sub-dataset to maximize downstream task performance, by aligning some DVs from the retrived co-training dataset with those from the target dataset. For example, we study whether retrieving demonstrations from DROID that have aligned camera poses with that of the downstream setup will improve learning performance.

To perform this study with minimal confounders, we design multiple datasets performing the same task in target and co-training, with the co-training datasets containing high variation in all DVs and sometimes aligned along one DV to understand the importance of alignment in that DV. Similar to the collector's study, we design different distributions of the target DV and co-training DVs, but this time the distribution of all the remaining DVs are highly varied.

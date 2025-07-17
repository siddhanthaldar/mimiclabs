# Fixtures

We list here all supported fixtures that are currently supported in MimicLabs, and their respective configs for placement arrangements.

Credits to the authors of LIBERO for setting up the base assets that enabled us to expand on.

## Cabinets

### Specifying cabinet placement

You can specify the placement region of a cabinet as in the example below:
```
(:regions
    (cabinet_init_region
        (:target table)
        (:ranges (
                (-0.01 0.39 0.01 0.41)
            )
        )
        (:yaw_rotation (
                (0.0 0.0)
            )
        )
    )
)
(:fixtures
    table - table
    cabinet_1 - metal_cabinet
)
```
This initializes a `metal_cabinet` (named `cabinet_1`) in the xy range `(-0.01 0.39 0.01 0.41)` with respect to the `table`.

You can change type of cabinet by specifying in `:fixtures` a cabinet name from the following list of available cabinets:
- `colorful_cabinet`
- `metal_cabinet`
- `wooden_cabinet`
- `white_cabinet`
- `blue_cabinet`
- `marble_cabinet`
- `lava_cabinet`
- `light_wood_cabinet`

### Specifying drawer within cabinets

You can specify the drawer of significance for your task by stating the appropriate region in `:regions` as in the example below:
```
(:regions
    (cabinet_init_region
        (:target table)
        (:ranges (
                (-0.01 0.39 0.01 0.41)
            )
        )
        (:yaw_rotation (
                (0.0 0.0)
            )
        )
    )
    (top_region
        (:target cabinet_1)
    )
)
(:fixtures
    table - table
    cabinet_1 - metal_cabinet
)
```
This initializes a `metal_cabinet` instance with the top-drawer specified as `top_region`.

You can specify the drawer of interest by specifying one of the following regions for the 3-drawer cabinet:
- `top_region`
- `middle_region`
- `bottom_region`


## Microwaves

### Specifying microwave placement

You can specify the placement region of a microwave as in the example below:
```
(:regions
    (microwave_init_region
        (:target table)
        (:ranges (
                (0.25 -0.01 0.30 0.01)
            )
        )
        (:yaw_rotation (
                (-1.65806 -1.48353)
            )
        )
    )
)
(:fixtures
    table - table
    microwave_1 - microwave
)
```
This initializes a `microwave` (named `microwave_1`) in the xy range `(0.25 -0.01 0.30 0.01)` and yaw range `(-1.65806 -1.48353)` with respect to the `table`.

You can change type of microwave by specifying in `:fixtures` a microwave name from the following list of available microwaves:
- `microwave`
- `microwave_2`
- `microwave_3`
- `microwave_4`
- `microwave_5`
- `microwave_6`
- `microwave_7`
- `microwave_8`


### Specifying regions for microwaves

You can specify the region of interest within the microwave for your task by stating the appropriate region in `:regions` as in the example below:
```
(:regions
    (microwave_init_region
        (:target table)
        (:ranges (
                (0.25 -0.01 0.30 0.01)
            )
        )
        (:yaw_rotation (
                (-1.65806 -1.48353)
            )
        )
    )
    (heating_region
        (:target microwave_1)
    )
)
(:fixtures
    table - table
    microwave_1 - microwave
)
```
This initializes a `microwave` instance with the heating region specified as `heating_region`.

You can specify the region of interest by specifying one of the following regions for the microwave:
- `heating_region` - region inside the microwave
- `top_side` - region above the microwave


## Coffee Machine

### Specifying coffee machine placement

You can specify the coffee machine in your task config as follows:
```
(:regions
    (coffee_machine_init_region
        (:target table)
        (:ranges (
                (-0.2 0.25 -0.1 0.35)
            )
        )
        (:yaw_rotation (
                (0.4 0.45)
            )
        )
    )
)
(:objects
    coffee_machine_1 - coffee_machine
)
```
This initializes a `coffee_machine` (named `coffee_machine_1`) in the xy range `(-0.2 0.25 -0.1 0.35)` and yaw range `(0.4 0.45)` with respect to the `table`.

We currently only support one coffee machine:
- `coffee_machine`

### Specifying regions within the coffee machine

You can specify the region of interest within the coffee machine for your task by stating the appropriate region in `:regions` as in the example below:
```
(:regions
    (coffee_machine_init_region
        (:target table)
        (:ranges (
                (-0.2 0.25 -0.1 0.35)
            )
        )
        (:yaw_rotation (
                (0.4 0.45)
            )
        )
    )
    (pod_region
        (:target coffee_machine_1)
    )
)
(:objects
    coffee_machine_1 - coffee_machine
)
```
This initializes a `coffee_machine` instance with region where a pod is supposed to go specified as `pod_region`.

The coffee machine currently supports one region:
- `pod_region`

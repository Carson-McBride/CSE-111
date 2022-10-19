"""
storage_efficiency = 
volume
surface_area
In other words, the storage efficiency of a can is the space inside the can divided by the amount of steel required to make the can. The formulas for the volume and surface area of a cylinder are:

volume = π radius**2 * height
surface_area = 2π *radius *(radius + height)

"""


from math import pi


def main():
    name = "#1 Picnic"
    radius = 6.83
    height = 10.16
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_effiency = compute_storage_efficiency(volume, surface_area)
    print(f"Name: {name}, Storage Efficiency {storage_effiency:.2f}")

    name = "#1 Tall"
    radius = 7.78
    height = 11.91
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_effiency = compute_storage_efficiency(volume, surface_area)
    print(f"Name: {name}, Storage Efficiency {storage_effiency:.2f}")

    name = "#2"
    radius =8.73
    height = 11.59
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_effiency = compute_storage_efficiency(volume, surface_area)
    print(f"Name: {name}, Storage Efficiency {storage_effiency:.2f}")


    name = "#2.5"
    radius =10.32
    height = 11.91
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_effiency = compute_storage_efficiency(volume, surface_area)
    print(f"Name: {name}, Storage Efficiency {storage_effiency:.2f}")


    name = "#3 Cylinder"
    radius =10.79
    height = 17.78
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_effiency = compute_storage_efficiency(volume, surface_area)
    print(f"Name: {name}, Storage Efficiency {storage_effiency:.2f}")


    name = "#5"
    radius =13.02
    height = 14.29
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_effiency = compute_storage_efficiency(volume, surface_area)
    print(f"Name: {name}, Storage Efficiency {storage_effiency:.2f}")


    name = "#6Z"
    radius = 5.40
    height = 8.89
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_effiency = compute_storage_efficiency(volume, surface_area)
    print(f"Name: {name}, Storage Efficiency {storage_effiency:.2f}")


    name = "#8Z short"
    radius = 6.83
    height = 7.62
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_effiency = compute_storage_efficiency(volume, surface_area)
    print(f"Name: {name}, Storage Efficiency {storage_effiency:.2f}")


    name = "#10"
    radius = 15.72
    height = 17.78
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_effiency = compute_storage_efficiency(volume, surface_area)
    print(f"Name: {name}, Storage Efficiency {storage_effiency:.2f}")


    name = "#211"
    radius = 6.83
    height = 12.38
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_effiency = compute_storage_efficiency(volume, surface_area)
    print(f"Name: {name}, Storage Efficiency {storage_effiency:.2f}")


    name = "#300"
    radius = 7.62
    height = 11.27
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_effiency = compute_storage_efficiency(volume, surface_area)
    print(f"Name: {name}, Storage Efficiency {storage_effiency:.2f}")


    name = "#303"
    radius = 8.10
    height = 11.11
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_effiency = compute_storage_efficiency(volume, surface_area)
    print(f"Name: {name}, Storage Efficiency {storage_effiency:.2f}")



    return 

def compute_volume(radius, height):
    volume = pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2*pi *radius *(radius + height)
    return surface_area 

def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency
main()
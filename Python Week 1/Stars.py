def draw_stars(arr):
    for x in arr:
        print "*" * x

nums = [4, 6, 1, 3, 5, 7, 25]
draw_stars(nums)


def draw_stars(arr):
    for x in arr:
        if isinstance(x, int):
            print "*" * x
        elif isinstance (x,str):
            length = len(x)
            letter = x[0].lower()
            print letter * length

nums = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(nums)

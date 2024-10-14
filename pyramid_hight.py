def calculate_pyramid_height(blocks):
    height = 0
    current_layer = 1
    
    while blocks >= current_layer:
        blocks -= current_layer
        height += 1
        current_layer += 1
    
    return height

# Input: number of blocks
blocks = int(input("Enter the number of blocks: "))

# Output: height of the pyramid
pyramid_height = calculate_pyramid_height(blocks)
print("The height of the pyramid is:", pyramid_height)

def generate_noise_image(content_image, noise_ratio = CONFIG.NOISE_RATIO):
    
    # Generate a random noise_image
    noise_image = np.random.uniform(-20, 20, (1, CONFIG.IMAGE_HEIGHT, CONFIG.IMAGE_WIDTH, CONFIG.COLOR_CHANNELS)).astype('float32')
    
    # Set the input_image to be a weighted average of the content_image and a noise_image
    input_image = noise_image * noise_ratio + content_image * (1 - noise_ratio)
    
    return input_image


#mean = mean(average)
def reshape_and_normalize_image(image):
    
    # Reshape image 
    image = np.reshape(image, ((1,) + image.shape))
    
    # Substract the mean 
    
    image = image - mean
    
    return image


def save_image(path, image):
    
    # Un-normalize the image so that it looks good
    image = image + mean
    
    # Clip and Save the image
    image = np.clip(image[0], 0, 255).astype('uint8')
    scipy.misc.imsave(path, image)

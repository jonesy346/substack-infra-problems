"""
Question:

A consumer processes uploaded images. Occasionally image processing fails because of transient network issues. Design a retry mechanism that retries failed messages up to 3 times before moving them to a dead-letter queue.

Answer:

We'll use a hash table to store the retry count for a particular image. When an image processing fails, we check the retry count. If it's less than or equal to 3, we retry processing the image. If it exceeds 3, we move the image to a dead-letter queue for further investigation or manual handling.
"""

class ImageProcessor:
    def __init__(self):
        self.dead_letter_queue = []

    def process_image(self, image_id):
        max_retries = 3
        for attempt in range(max_retries + 1):
            try:
                if self.simulate_processing_failure():
                    raise Exception("Transient network issue")
                print(f"Image {image_id} processed successfully.")
                return
            except Exception as e:
                print(f"Error processing image {image_id}: {e}")
                if attempt < max_retries:
                    print(f"Retrying image {image_id} (Attempt {attempt + 1})...")
                else:
                    print(f"Moving image {image_id} to dead-letter queue after {max_retries} retries.")
                    self.dead_letter_queue.append(image_id)

    def simulate_processing_failure(self):
        import random
        return random.choice([True, False])
    
processor = ImageProcessor()
for i in range(1, 6):
    processor.process_image(f"image_{i}")
print("Dead-letter queue:", processor.dead_letter_queue)

"""
Author: Chukwunazaekpere Emmanuel Obioma
Lecture: Parallelism
Nationality: Biafran
Email-1: chukwunazaekpere.obioma@ue-germany.de 
Email-2: ceo.naza.tech@gmail.com
************************************************
Implementation: to implement the sequential multiplication of squared matrices
Course: Multi-core Programming
Written: Oct 21st 2024
Due: Oct 23rd 2024
"""

from datetime import datetime
import random
from time import time
import logging
logger = logging.getLogger(__name__)
log_date = datetime.now()
logging.basicConfig(level=logging.INFO)

class SequentialCounter():
    """This class implements a sequential counter, for counting the occurence of elements in an array"""
    def __init__(self):
        self.array_length = 0

    def get_array_size(self):
        """Get size of array from user"""
        logging.info(msg=f"\n\t {datetime.now()} This is the sequential counter program...")
        try:
            array_length = input("\n\t Please enter the size of array to be generated: ")
            self.array_length = int(array_length)
        except Exception as err:
            return f"Array size unacceptable. Please enter a number."
        
    def generate_array_elements(self):
        """Generate random elements to fill array"""
        self.get_array_size()
        array = []
        for val in range(0, self.array_length):
            array.append(random.randint(2, 100)) # generate random array elements between 2 & 100
        return array
    
    
    def count_elements_occurrences(self):
        """Count elements occurrences in generated aarray"""
        generated_array = self.generate_array_elements()
        print("\n\t generated_array: ", generated_array)
        counter_dict = {}
        for elemnts in generated_array:
            try:
                counter_dict[str(elemnts)] = counter_dict[str(elemnts)]+1
            except:
                counter_dict = {**counter_dict, f"{str(elemnts)}": 1}
        return counter_dict
    

if __name__ == "__main__":
    counter = SequentialCounter()
    start_time = time()
    elements_occurrences = counter.count_elements_occurrences()
    logging.info(msg=f"\n\t Elements occurence: {elements_occurrences}")
    logging.info(msg=f"\n\t total time taken: {(time()-start_time)} secs")


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
from omp4py import *

from datetime import datetime
import random
from time import time
import logging
logger = logging.getLogger(__name__)
log_date = datetime.now()
logging.basicConfig(level=logging.INFO)




def get_array_size():
    """Get size of array from user"""
    try:
        array_length = input("\n\t Please enter the size of array to be generated: ")
        return int(array_length)
    except Exception as err:
        logging.info(msg=f"\n\t Array size unacceptable. Please enter a number.")
        return 0

def generate_array_elements(array_length):
    """Generate random elements to fill array"""
    array = []
    for val in range(0, array_length):
        array.append(random.randint(2, 100)) # generate random array elements between 2 & 100
    return array


@omp
def occureence_arrangement(array):
    print("\n\t counter_dict: array", array)
    counter_dict = {}
    for elemnts in array:
        try:
            counter_dict[str(elemnts)] = counter_dict[str(elemnts)]+1
        except:
            counter_dict = {**counter_dict, f"{str(elemnts)}": 1}
    print("\n\t counter_dict: ", counter_dict)
    return counter_dict

@omp
def count_elements_occurrences(array_length):
    """Count elements occurrences in generated aarray"""
    generated_array = generate_array_elements(array_length)
    # print("\n\t generated_array: ", generated_array)
    first_half = len(generated_array)//2
    counter_dict1 = {}
    counter_dict2 = {}
    counter_occ = {}
    with omp("parallel"): # parallel region
        with omp("sections"): # job sharing
            with omp("section"): # share first half of generated list 
                counter_dict1 = occureence_arrangement(generated_array[0:first_half])
            with omp("section"): # share last half of the generated list 
                counter_dict2 = occureence_arrangement(generated_array[first_half:len(generated_array)-1])
    dict1_keys = counter_dict1.keys()
   
   


    print("\n\t counter_occ: ", counter_occ)
    
    return counter_dict2
    

if __name__ == "__main__":
    array_length = get_array_size()
    start_time = time()
    elements_occurrences = count_elements_occurrences(array_length)
    logging.info(msg=f"\n\t Elements occurence: {elements_occurrences}")
    logging.info(msg=f"\n\t total time taken: {(time()-start_time)} secs")


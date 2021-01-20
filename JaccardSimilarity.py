import numpy as np
from nltk.book import *

#S1 = set(word.lower() for word in text1)
#S2 = set(word.lower() for word in text2)
#S3 = set(word.lower() for word in text3)

class MinHash():
    
    def __init__(self, hash_functions):
        file1 = set(word.lower() for word in text1)
        file2 = set(word.lower() for word in text2)
        file3 = set(word.lower() for word in text3)
        self.all_words = list(file1 | file2 | file3)
        self.files = [file1, file2, file3]
        self.hash_functions_nr = hash_functions
        self.words_nr = len(self.all_words)
        self.files_nr = len(self.files)

        
    def get_characteristic_matrix(self):
        
        """columns of the matrix correspond to sets,
        and the rows correspond to elements of the universal set
        from which elements of the sets are drawn"""
        
        characteristic_matrix = np.zeros((self.words_nr, self.files_nr))
        for i in range(len(self.all_words)):
            for j in range(len(self.files)):
                if self.all_words[i] in self.files[j]:
                    characteristic_matrix[i][j] = 1
        return characteristic_matrix
    
    
    def get_hash_matrix(self):
        
        """create matrix of given length filled with hash functions family"""
        
        hash_matrix = np.zeros((self.words_nr, self.hash_functions_nr))
        for i in range(self.words_nr):
            for j in range(self.hash_functions_nr):
                hash_matrix[i][j] = (2*(j+2)*(i+1) + 1) % self.words_nr
        return hash_matrix
    
    
    def get_signature_matrix(self):
            
        """from characteristic matrix M form a signature matrix,
        in which the i-th column of M is replaced by the minhash signature for (the set of)
        the i-th column"""
        
        signature_matrix = np.ones((self.hash_functions_nr, self.files_nr))*np.inf
        characteristic_matrix = self.get_characteristic_matrix()
        hash_matrix = self.get_hash_matrix()
        
        for i in range(self.words_nr):
            for j in range(self.files_nr):
                if characteristic_matrix[i][j] == 1:
                    for k in range(self.hash_functions_nr):
                        hash_row = hash_matrix[i,:]
                        h_i = hash_row[k]
                        if h_i < signature_matrix[k,j]:
                                signature_matrix[k,j] = h_i
        return signature_matrix
       
        
    def jaccard_similarity(self):
        """get the jaccard similarity between two files"""
        
        results = []
        signature_matrix = self.get_signature_matrix()
        for x in range(self.files_nr):
            for y in range(x + 1, self.files_nr):
                count = 0
                sig1 = signature_matrix[:, x]
                sig2 = signature_matrix[:, y]
                for i in range(len(sig1)):
                    if sig1[i] == sig2[i]:
                        count += 1
                results.append((f"Similarity of file{x +1} and file{y+1}: ", count/(len(sig1)+len(sig2))))
        return results
    
    
    
if __name__ == '__main__':
    
    minhash = MinHash(100)
    similarities = minhash.jaccard_similarity()
    [print(str(result[0]) + str(result[1]) + "\n") for result in similarities]











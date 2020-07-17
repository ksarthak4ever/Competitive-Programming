class RansomHelper(object):
    def __init__(self, ransom_text, magazine_text):
        """ 
        Initialize RansomNote and MagazineText 
        """
        self.ransom_text = ransom_text.lower()
        self.magazine_text = magazine_text.lower()

    def _count_words_in_string(self, sentence):
        """
        Private helper method to count the
        number of occurances of words in sentences
        :type sentence: string
        :rtype: HashMap object
        """
        word_count = dict()
        for i in sentence:
            if word_count.get(i) is None:
                word_count[i] = 1
            else:
                word_count[i] = word_count.get(i)+1

        return word_count

    def can_generate_ransom_note(self):
        """ 
        Returns True if ransom note can be generated using 
        the magazine text or else return False
        :rtype: boolean i.e True or False
        """
        if self.ransom_text == '' or self.ransom_text == ' ':
            return True
        ransom_text_words = self.ransom_text.split(' ')
        magazine_text_words = self.magazine_text.split(' ')
        # counting the occurrences of words in the ransom and magazine texts.
        ransom_count = self._count_words_in_string(ransom_text_words)
        magazine_count = self._count_words_in_string(magazine_text_words)
        result = False
        for i in ransom_text_words:
            # if magazine_count hashmap doesn't have word
            if magazine_count.get(i) is None:
                result = False
                break
            # if ransom_count hashmap have less word occurances than magazine count.
            if ransom_count.get(i) <= magazine_count.get(i):
                result = True
            else:
                result = False
                break
        return result

if __name__ == "__main__":
    result = RansomHelper(ransom_text='one two two three three three four four four', magazine_text='four four four three three three two two one')
    result.can_generate_ransom_note()
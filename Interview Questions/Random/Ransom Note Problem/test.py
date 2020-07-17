import unittest

from ransom import RansomHelper


class TestRansomHelper(unittest.TestCase):
    def test_ransom_helper(self):
        self.assertTrue(
            RansomHelper(
                'Send Five Million Dollars In Cash By 5 PM Tomorrow',
                '''
                    This is a text in the popular Time Magazine.
                    Time magazine is ranked top magazine of the world since last 5 years.
                    British PM Boris Johnson is scheduled to give a speech on CoVid 19 situation
                    tomorrow at town hall.He needs to set aside five million dollars for the PPE
                    of front line workers. You can send cash to your family by using Western Union now.
                '''
            ).can_generate_ransom_note())
        self.assertFalse(RansomHelper('million million', 'million').can_generate_ransom_note())
        self.assertTrue(RansomHelper('million million', 'million million million').can_generate_ransom_note())
        self.assertFalse(RansomHelper('million billion million', 'million million').can_generate_ransom_note())
        self.assertFalse(
            RansomHelper(
                'Send Five Million Dollars In Cash By 5 PM Tomorrow',
                '''
                    Lorem Ipsum is simply dummy text of the printing and typesetting industry.
                    It might contain some junk, which doesn't make sense, like who talks about having
                    five million dollars in cash.
                '''
                ).can_generate_ransom_note())
        self.assertTrue(RansomHelper('', 'million million').can_generate_ransom_note())
        self.assertFalse(RansomHelper('million this this that', 'million this that').can_generate_ransom_note())
        self.assertTrue(RansomHelper('one two two three three three four four four',
                             'four four four three three three two two one').can_generate_ransom_note())



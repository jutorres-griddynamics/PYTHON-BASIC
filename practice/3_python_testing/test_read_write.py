"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import unittest
import tempfile
import filecmp
class TestSum(unittest.TestCase):

    def test_check_text(self):
        desiredOutput = "80, 37, 15, 14, 99, 99, 59, 90, 69, 39, 67, 91, 74, 40, 32, 82, 48, 1, 95, 66"

        with open("../2_python_part_2/files/result.txt") as opened_file:
            for line in opened_file:
                self.assertEqual(line,desiredOutput, "Not the expected output.")

if __name__ == '__main__':
    unittest.main()
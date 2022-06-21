"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import unittest
import tempfile
import filecmp
class TestSum(unittest.TestCase):

    def test_assert_equal(self):
        line1 = ""
        line2 = ""
        with open("../2_python_part_2/file1") as opened_file:
            for line in opened_file:
                line1 = line
        with open("../2_python_part_2/file2") as opened_file:
            for line in opened_file:
                line2 = line
        line1 = line1.split("/")
        line2 = line.split("-")
        line2.reverse()
        self.assertEqual(line1, line2, "Not the same result.")

if __name__ == '__main__':
    unittest.main()
    print("All right!")
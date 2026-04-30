# Test case
import unittest

from src.config import config
from ok.test.TaskTestCase import TaskTestCase

from src.tasks.MyOneTimeTask import MyOneTimeTask


class TestMyOneTimeTask(TaskTestCase):
    task_class = MyOneTimeTask

    config = config

    def test_ocr1(self):
        # Create a BattleReport object
        texts = self.ocr(x=0.6, y=0.7407, to_x=0.6510, to_y=0.787)
        self.log_info(texts)

    # def test_ocr2(self):
    #     # Create a BattleReport object
    #     self.set_image('tests/images/main.png')
    #     text = self.task.find_some_text_with_relative_box()
    #     self.assertEqual(text[0].name, '招募')

    # def test_feature1(self):
    #     # Create a BattleReport object
    #     self.set_image('tests/images/main.png')
    #     feature = self.task.test_find_one_feature()
    #     self.assertIsNone(feature)

    # def test_feature2(self):
    #     # Create a BattleReport object
    #     self.set_image('tests/images/main.png')
    #     features = self.task.test_find_feature_list()
    #     self.assertEqual(0, len(features))


if __name__ == '__main__':
    unittest.main()

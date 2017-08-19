from django.test import TestCase
from tracker.models import Board

class TestBoard(TestCase):
    """This class defines the test suite for the Board model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.board_name = "test board"
        self.board = Board(name=self.board_name)

    def test_model_can_create_a_board(self):
        """Test the Board model can create a board."""
        old_count = Board.objects.count()
        self.board.save()
        new_count = Board.objects.count()
        self.assertNotEqual(old_count, new_count)
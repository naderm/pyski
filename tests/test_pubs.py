
import unittest

import pyski


class UtilTestCase(unittest.TestCase):
    def test_list_publications(self):
        pubs = pyski.list_publications()
        self.assertGreater(
            len(pubs),
            0,
        )

        for pub_id in pubs:
            self.assertIsInstance(pub_id, int)

    def test_get_publication(self):
        # API Announcement Post
        pub_id = 266825

        pub = pyski.get_publication(pub_id)

        self.assertEqual(
            pub["id"],
            pub_id,
        )

        self.assertEqual(
            pub["user"],
            "rob05c",
        )

        for comment_id in pub["kids"]:
            comment = pyski.get_publication(comment_id)

            self.assertIsNotNone(
                comment,
            )

    def test_list_endpoints(self):
        endpoints = pyski.list_endpoints()

        self.assertIn(
            "/publications",
            endpoints,
        )
        self.assertIn(
            "/publication/{id}",
            endpoints,
        )
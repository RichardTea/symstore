import mock
import unittest
import symstore


class TestSetup(unittest.TestCase):
    @mock.patch("setuptools.setup")
    def test_setup(self, setup_mock):
        import setup  # noqa

        setup_mock.assert_called_once_with(
            name="symstore",
            version=symstore.VERSION,
            description=mock.ANY,
            long_description=mock.ANY,
            long_description_content_type="text/markdown",
            url=mock.ANY,
            classifiers=mock.ANY,
            license="MIT",
            keywords=mock.ANY,
            packages=mock.ANY,
            package_data=mock.ANY,
            data_files=[("", ["LICENSE"])],
            entry_points=mock.ANY,
            extras_require=mock.ANY)

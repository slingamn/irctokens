import unittest
import irctokens

class FormatTestTags(unittest.TestCase):
    def test(self):
        line = irctokens.format("PRIVMSG", ["#channel", "hello"],
            tags={"id": "\\" + " " + ";" + "\r\n"})
        self.assertEqual(line, "@id=\\\\\\s\\:\\r\\n PRIVMSG #channel hello")

    def test_missing(self):
        line = irctokens.format("PRIVMSG", ["#channel", "hello"])
        self.assertEqual(line, "PRIVMSG #channel hello")

    def test_none_value(self):
        line = irctokens.format("PRIVMSG", ["#channel", "hello"],
            tags={"a": None})
        self.assertEqual(line, "@a PRIVMSG #channel hello")

    def test_empty_value(self):
        line = irctokens.format("PRIVMSG", ["#channel", "hello"],
            tags={"a": ""})
        self.assertEqual(line, "@a PRIVMSG #channel hello")

class FormatTestSource(unittest.TestCase):
    def test(self):
        line = irctokens.format("PRIVMSG", ["#channel", "hello"],
            source="nick!user@host")
        self.assertEqual(line, ":nick!user@host PRIVMSG #channel hello")

class FormatTestCommand(unittest.TestCase):
    def test_lowercase(self):
        line = irctokens.format("privmsg")
        self.assertEqual(line, "PRIVMSG")

class FormatTestTrailing(unittest.TestCase):
    def test_space(self):
        line = irctokens.format("PRIVMSG", ["#channel", "hello world"])
        self.assertEqual(line, "PRIVMSG #channel :hello world")

    def test_no_space(self):
        line = irctokens.format("PRIVMSG", ["#channel", "helloworld"])
        self.assertEqual(line, "PRIVMSG #channel helloworld")

class FormatTestSpacedArg(unittest.TestCase):
    def test(self):
        def _inner():
            irctokens.format("USER", ["user", "0 *", "real name"])
        self.assertRaises(ValueError, _inner)

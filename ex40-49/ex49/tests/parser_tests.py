from nose.tools import *
from ex49.parser import * 
from ex49.lexicon import *

def test_peek():
    result = scan('north')
    assert_equal(peek(result), 'direction')

def test_match():
    assert_equal(match([('noun', 'player')], 'noun'), ('noun', 'player'))

def test_skip():
    result = scan('north')
    assert_equal(result, [('direction', 'north')])

def test_parse_verb():
    with assert_raises_regexp(ParserError, "Expected a verb next."):
        parse_verb(['noun', 'player'])

def test_parse_object():
    with assert_raises_regexp(ParserError, 
            "Expected a noun or direction next."):
        parse_object([('error', 'IAS')])

def test_parse_subject():
    assert_equal(parse_subject([('verb', 'run')]), ('noun', 'player'))
    with assert_raises_regexp(ParserError, "Expected a verb next."): 
        parse_subject(['noun', 'player'])

def test_parse_sentence():
    pass
"""
    # TODO: Fix this test.
    assert_equal(parse_sentence([('verb', 'run')]), [('verb', 'run')])
    test_sentence = parse_sentence([('verb', 'run'),
            ('direction', 'north'),
            ('error', 'IAS')])
    assert_equal(test_sentence, [('verb', 'run'),
        ('direction', 'north'),
        ('error', 'IAS')])
"""

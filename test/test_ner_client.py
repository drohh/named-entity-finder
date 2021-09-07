import unittest
from ner_client import NamedEntityClient
from test_doubles import NerModelTestDouble



class TestNerClient(unittest.TestCase):

    ''' 
    NER client should return
        { ents: [{...}],
          html: "<div>..." }
    '''

    def test_get_ents_returns_dict_given_empty_string_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dict_given_nonempty_string_causes_empty_spact_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Caitlyn is a person in Louisiana.")
        self.assertIsInstance(ents, dict)

    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Laurent Fressinet', 'label_':'PERSON'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents':[{'ent':'Laurent Fressinet','label':'Person'}],
                        'html':""}
        self.assertListEqual(result['ents'], expected_result['ents'])      

    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_Group(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'African', 'label_':'NORP'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents':[{'ent':'African','label':'Group'}],
                        'html':""}
        self.assertListEqual(result['ents'], expected_result['ents'])      

    def test_get_ents_given_spacy_LOC_is_returned_serializes_to_Location(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'the forest', 'label_':'LOC'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents':[{'ent':'the forest','label':'Location'}],
                        'html':""}
        self.assertListEqual(result['ents'], expected_result['ents'])      

    def test_get_ents_given_spacy_GPE_is_returned_serializes_to_Location(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Germany', 'label_':'GPE'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents':[{'ent':'Germany','label':'Location'}],
                        'html':""}
        self.assertListEqual(result['ents'], expected_result['ents'])      
    
    def test_get_ents_given_spacy_LANGUAGE_is_returned_serializes_to_Language(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'German', 'label_':'LANGUAGE'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents':[{'ent':'German','label':'Language'}],
                        'html':""}
        self.assertListEqual(result['ents'], expected_result['ents'])      

    def test_get_ents_given_multiple_ents_serializes_all(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'German', 'label_':'LANGUAGE'},
                    {'text':'Germany', 'label_':'GPE'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = { 'ents':
                            [{'ent': 'German', 'label':'Language'},
                             {'ent': 'Germany', 'label':'Location'}],
                            'html':""}
        self.assertListEqual(result['ents'], expected_result['ents'])      


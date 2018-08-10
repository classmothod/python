import nltk
import sys
sys.path.insert(0, "../Date/TextProcessing")
from TextProcessing import *


class AM:

	def __init__(self):

		self.base = Musics()
		self.WordList = []

		for y in self.base:
			self.WordList.append(y)


		self.stopWordsNLTK = nltk.corpus.stopwords.words('portuguese')
		self.Stemmer = nltk.stem.RSLPStemmer()
		self.stopWords = ['a']
		self.FraseStemming = self.TakeRadical()

	def AddStopWords(self):
		for y in self.stopWords:
			self.stopWordsNLTK.append(y)

	def AddWords(self, Words):
		for y in Words:
			self.stopWords.append(y)

	def TakeRadical(self):
		Base = self.WordList
		PhraseStemmer = []
		for (Phrase, Pulse) in Base:
			Scroll = []
			for Word in Phrase.split():
				if Word not in self.stopWordsNLTK:
					Radical = self.Stemmer.stem(Word)
					if len(Radical) < 4:
						Scroll.append(Word[0:4])
					else:
						Scroll.append(Radical)
			Scroll = (Scroll, Pulse)
			PhraseStemmer.append(Scroll)
		return PhraseStemmer

	def ReturnWords(self):
		Phrases = self.FraseStemming
		allWords = []
		for (Phrase, Pulse) in Phrases:
			allWords.extend(Phrase)
		return allWords

	def ReturnFrequency(self):
		Words = nltk.FreqDist(self.ReturnWords())
		return Words

	def SingleWords(self):
		Frequency = self.ReturnFrequency().keys()
		return Frequency

	def ExtractWords(self, documento):
		Doc = set(documento)
		Characteristics = {}
		for Word in self.SingleWords():
			Characteristics['%s' % Word] = (Word in Doc)
		return Characteristics

	def Sorted(self, Nivel=10):
		BaseComplet = nltk.classify.apply_features(self.ExtractWords, self.FraseStemming)
		Classify =  nltk.NaiveBayesClassifier.train(BaseComplet)
		print(Classify.show_most_informative_features(Nivel))

	def Mining(self, Phrase):
		BaseComplet = nltk.classify.apply_features(self.ExtractWords, self.FraseStemming)
		Classify =  nltk.NaiveBayesClassifier.train(BaseComplet)

		ListPhrase = []
		for Word in Phrase.split():
			if Word not in self.stopWordsNLTK:
				Radical = self.Stemmer.stem(Word)
				if len(Radical) < 4:
					ListPhrase.append(Word[0:4])
				else:
					ListPhrase.append(Radical)
		New = self.ExtractWords(ListPhrase)
		Cy = Classify.classify(New)
		print('Phrase:', Phrase)
		print('Classificado como:', Cy)

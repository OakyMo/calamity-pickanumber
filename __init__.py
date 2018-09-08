#Copyright (C) 2018  Arc676/Alessandro Vinciguerra <alesvinciguerra@gmail.com>

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation (version 3)

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG, getLogger

from random import randint

__author__ = 'Arc676/Alessandro Vinciguerra'
LOGGER = getLogger(__name__)

class NumberGuessSkill(MycroftSkill):

	lowerBound = 0
	upperBound = 100
	answer = 0
	userGuess = 0

	@intent_handler(IntentBuilder("").require("NumberGuess").optionally("Play").optionally("Suggest"))
	def handle_start_game_intent(self, message):
		self.speak_dialog("start.game")
		# get lower bound
		while True:
			lowerBound = self.get_response("get.lower")
			try:
				lowerBound = int(lowerBound)
				break
			except ValueError:
				self.speak_dialog("invalid.input")
		# get upper bound
		while True:
			upperBound = self.get_response("get.upper")
			try:
				upperBound = int(upperBound)
				break
			except ValueError:
				self.speak_dialog("invalid.input")
		answer = randint(lowerBound, upperBound)
		userGuess = lowerBound - 1
		while userGuess != answer:
			userGuess = self.get_response("guess")
			try:
				userGuess = int(userGuess)
			except ValueError:
				self.speak_dialog("invalid.input")
				continue
			if userGuess < answer:
				self.speak_dialog("too.low")
			elif userGuess > answer:
				self.speak_dialog("too.high")
		self.speak_dialog("correct")

	def stop(self):
		lowerBound, upperBound = 0, 100
		answer = 0
		userGuess = answer
		return True

def create_skill():
	return NumberGuessSkill()

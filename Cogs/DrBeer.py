import asyncio
import discord
import random
from   discord.ext import commands

# This is the Uptime module. It keeps track of how long the bot's been up

class DrBeer:

	# Init with the bot reference, and a reference to the settings var
	def __init__(self, bot):
		self.bot = bot

	def message(self, message):
		# Check the message and see if we should allow it - always yes.
		# This module doesn't need to cancel messages.
		return { 'Ignore' : False, 'Delete' : False}

	@commands.command(pass_context=True)
	async def drbeer(self, ctx):
		"""Put yourself in your place."""
		beerList = ["Hey, yall. Quit ya horsin' around now. Can't you see I'm busy tryin'a shoot'n all them summersquash?",
					"Now I don't know how to use all them 5-dollah words y'all sprayin' around, but sure seems to me like y'all need to mind your peas and queues.",
					"As long as I can keep practicin' and protectin' all my favorite amendments, like the second and thirty-first, I am all dandy.",
					"Woah there, buckaroo! That's a mighty harsh language from someone communicating through a tube in the ocean over the internets.",
					"Now, I don't mind y'all people, but you keep botherin' me when I'm tryin'a enjoy my cold Bud in this beautiful, patriotic sunset. Haven't yall folks got better things to do then keep arguing and snicker in' around when y'all should be worried about the government and the N, S & A listenin'?",
					"Well, my daddy always said a man is only as good as his words and the thrust and torque of his good ole John Deere."]
		randnum = random.randint(0, len(beerList)-1)
		msg = '{}'.format(beerList[randnum])
		await self.bot.send_message(ctx.message.channel, msg)
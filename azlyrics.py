import azapi

API = azapi.AZlyrics('google', accuracy=0.5)

track_names = ['Do I Wanna Know?', 'R U Mine?', 'One For The Road', 'Arabella', 'I Want It All', 'No. 1 Party Anthem', 'Mad Sounds', 'Fireside', "Why'd You Only Call Me When You're High?", 'Snap Out Of It', 'There’d Better Be A Mirrorball', 'I Ain’t Quite Where I Think I Am', 'Sculptures Of Anything Goes', 'Jet Skis On The Moat', 'Body Paint', 'The Car', 'Big Ideas', 'Hello You', 'Mr Schwartz', 'Perfect Sense', 'Brianstorm', 'Teddy Picker', 'D Is For Dangerous', 'Balaclava', 'Fluorescent Adolescent', 'Only Ones Who Know', 'Do Me A Favour', 'This House Is A Circus', 'If You Were There, Beware', 'The Bad Thing', 'The View From The Afternoon', 'I Bet You Look Good On The Dancefloor', 'Fake Tales Of San Francisco', 'Dancing Shoes', "You Probably Couldn't See For The Lights But You Were Staring Straight At Me", 'Still Take You Home', 'Riot Van', 'Red Light Indicates Doors Are Secured', 'Mardy Bum', 'Perhaps Vampires Is A Bit Strong But…', 'My Propeller', 'Crying Lightning', 'Dangerous Animals', 'Secret Door', 'Potion Approaching', 'Fire And The Thud', 'Cornerstone', 'Dance Little Liar', 'Pretty Visitors', "The Jeweller's Hands", 'Star Treatment', 'One Point Perspective', 'American Sports', 'Tranquility Base Hotel & Casino', 'Golden Trunks', 'Four Out Of Five', "The World's First Ever Monster Truck Front Flip", 'Science Fiction', 'She Looks Like Fun', 'Batphone', 'Four Out Of Five - Live', 'Brianstorm - Live', 'Crying Lightning - Live', 'Do I Wanna Know? - Live', "Why'd You Only Call Me When You're High? - Live", '505 - Live', 'One Point Perspective - Live', 'Do Me A Favour - Live', 'Cornerstone - Live', 'Knee Socks - Live', 'Body Paint', 'There’d Better Be A Mirrorball', 'Do I Wanna Know?', '2013', "She's Thunderstorms", 'Black Treacle', 'Brick By Brick', 'The Hellcat Spangled Shalalala', "Don't Sit Down 'Cause I've Moved Your Chair", 'Library Pictures', 'All My Own Stunts', 'Reckless Serenade', 'Piledriver Waltz', 'Love is a Laserquest']

for i in range(0,len(track_names)):
	API.artist = 'Arctic Monkeys'
	API.title = track_names[i]
	API.getLyrics(save=False, ext='txt')
	f = open(f"lyrics/{API.title}.txt","w")
	f.write(API.lyrics)
	f.close()
	print(API.title + " -- done -- " + str(i+1) + " / " + str(len(track_names)))

# print(API.lyrics)

# Correct Artist and Title are updated from webpage
# print(API.title, API.artist)
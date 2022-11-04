import asyncio
from pyppeteer import launch
import urllib.parse
import string

def make_small(x):
    x = x.lower()
    b = "!@#$?.'’ "
    for char in b:
        x=x.replace(char,'')
    x = x.replace("-live","")
    return x + ".html"


async def main():
    # launch chromium browser in the background
    browser = await launch({"headless": False, "args": ["--start-maximized"]})
    # open a new tab in the browser
    for i in range(0,len(track_names)):
        page = await browser.newPage()
        # add URL to a new page and then open it
        print(make_small(track_names[i]))
        await page.goto("https://www.azlyrics.com/lyrics/arcticmonkeys/" + make_small(track_names[i]))

        

        # create a screenshot of the page and save it
        # await page.screenshot({"path": f"output/output{i}.png"})
    
    # close the browser
    await browser.close()

print("Starting...")
track_names = ['Do I Wanna Know?', 'R U Mine?', 'One For The Road', 'Arabella', 'I Want It All', 'No. 1 Party Anthem', 'Mad Sounds', 'Fireside', "Why'd You Only Call Me When You're High?", 'Snap Out Of It', 'There’d Better Be A Mirrorball', 'I Ain’t Quite Where I Think I Am', 'Sculptures Of Anything Goes', 'Jet Skis On The Moat', 'Body Paint', 'The Car', 'Big Ideas', 'Hello You', 'Mr Schwartz', 'Perfect Sense', 'Brianstorm', 'Teddy Picker', 'D Is For Dangerous', 'Balaclava', 'Fluorescent Adolescent', 'Only Ones Who Know', 'Do Me A Favour', 'This House Is A Circus', 'If You Were There, Beware', 'The Bad Thing', 'The View From The Afternoon', 'I Bet You Look Good On The Dancefloor', 'Fake Tales Of San Francisco', 'Dancing Shoes', "You Probably Couldn't See For The Lights But You Were Staring Straight At Me", 'Still Take You Home', 'Riot Van', 'Red Light Indicates Doors Are Secured', 'Mardy Bum', 'Perhaps Vampires Is A Bit Strong But…', 'My Propeller', 'Crying Lightning', 'Dangerous Animals', 'Secret Door', 'Potion Approaching', 'Fire And The Thud', 'Cornerstone', 'Dance Little Liar', 'Pretty Visitors', "The Jeweller's Hands", 'Star Treatment', 'One Point Perspective', 'American Sports', 'Tranquility Base Hotel & Casino', 'Golden Trunks', 'Four Out Of Five', "The World's First Ever Monster Truck Front Flip", 'Science Fiction', 'She Looks Like Fun', 'Batphone', 'Four Out Of Five - Live', 'Brianstorm - Live', 'Crying Lightning - Live', 'Do I Wanna Know? - Live', "Why'd You Only Call Me When You're High? - Live", '505 - Live', 'One Point Perspective - Live', 'Do Me A Favour - Live', 'Cornerstone - Live', 'Knee Socks - Live', 'Body Paint', 'There’d Better Be A Mirrorball', 'Do I Wanna Know?', '2013', "She's Thunderstorms", 'Black Treacle', 'Brick By Brick', 'The Hellcat Spangled Shalalala', "Don't Sit Down 'Cause I've Moved Your Chair", 'Library Pictures', 'All My Own Stunts', 'Reckless Serenade', 'Piledriver Waltz', 'Love is a Laserquest']

# print(track_names)

asyncio.get_event_loop().run_until_complete(main())

print("Screenshot has been taken")
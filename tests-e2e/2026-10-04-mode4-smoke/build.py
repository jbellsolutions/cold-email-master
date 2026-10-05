import json,re
L="https://experts.truerevenuepartnerships.com/?ref=LEADREF"
leads={}
def add(k,**kw): leads[k]=kw
add("five-star-auto-care-mentor@example.invalid",
F1=("ninety seconds","""Hey Shawn,

A reviewer wrote that their dad raved about your work on his 1964 Ford Falcon Futura.

I'd bet you can tell what an old car needs within ninety seconds of it rolling in. That takes years, and I doubt anyone has asked how.

I'm putting together the Real Experts Series, because it's not what you know. It's what you've seen. A 20 to 30 minute interview about what you've learned. No pitch, nothing hidden.

Reply and I'll send the three questions Justin, who hosts it, would ask you. If it's not for you, no problem.

Dana"""),
F1_FU=("ninety seconds","Hey Shawn, I forgot one thing. The edit comes to you first. It goes out once you say so. More is here:\n\n"+L+"\n\nWhat's one thing on an old car that nobody thinks to mention?"),
F2=("ask a machine","""Hey Shawn,

You opened a two bay shop in 2003, hoping to do custom high performance work.

A driver can ask a machine why a car hesitates under load and get a confident answer from something that has never held a wrench. You have.

That's why I'm doing the Real Experts Series. No matter how good AI gets, it can't replace what a veteran knows. It's a 20 to 30 minute interview about what you've seen.

Want the three questions Justin, who hosts it, would ask you? Just reply. Totally fine if the answer is no.

Dana"""),
F2_FU=("ask a machine","Hey Shawn, a scan tool tells you which code is stored. It never tells you what the code is leaving out, and nobody can look that up. What do you check first when a code points at the wrong part?"))
add("millennium-transmission-akron@example.invalid",
F1=("how you know","""Hey Ziad,

A reviewer wrote that you called a repair not worth doing, because of bigger problems underneath.

I'd bet you spot that kind of thing in ninety seconds, long before an estimate gets written. That takes years, and I doubt anyone has asked how.

The Real Experts Series is a 20 to 30 minute interview about what you've learned. It starts from one idea: it's not what you know. It's what you've seen. No pitch.

Reply and I'll send three questions written only for you. If you'd rather pass, I get it.

Dana"""),
F1_FU=("how you know","Hey Ziad, one more detail. You see the edit before anyone else. Nothing goes out until you approve it. The rest is here:\n\n"+L+"\n\nWhen a customer shows up sure of the problem, what do you ask first?"),
F2=("never done it","""Hey Ziad,

Your shop opened its doors in 1998, and you built it as a first generation family business.

A customer can ask a machine why a transmission slips and get a confident answer from something that has never rebuilt one. You have.

I'm doing the Real Experts Series for that reason. No matter how good AI gets, it can't replace what a veteran knows. Think of a 20 to 30 minute interview about what you've seen.

Hit reply and you'll have the three questions today. If now's a bad time, it can wait.

Dana"""),
F2_FU=("never done it","Hey Ziad, a rebuild can look perfect on the bench and still fail on the road, and no manual says which ones. What's the one sign you trust before a car ever reaches the lift?"))
add("auto-service-experts-grove-city@example.invalid",
F1=("ninety seconds","""Hey Mike,

A reviewer wrote that their pickup wouldn't start, and your shop found nothing wrong and charged only for the diagnostic.

I'd bet a no start story tells you its ending in ninety seconds. Years of that build it, and I doubt anyone has ever asked you how.

Here's the idea behind the Real Experts Series: it's not what you know. It's what you've seen. We talk for 20 to 30 minutes about what you've learned. No pitch, nothing hidden.

Just reply and I'll send the three questions we wrote for you. No is a fine answer too.

Dana"""),
F1_FU=("ninety seconds","Hey Mike, I left one thing out. Nothing goes out until you approve the edit. The page is here:\n\n"+L+"\n\nWhat do customers ask that you wish they'd asked sooner?"),
F2=("the confident answer","""Hey Mike,

Your team page says you've put in over 35 years at dealerships and independent shops.

A driver can ask a machine why a truck won't start and get a confident answer from something that has never stood in a cold bay. You have.

I'm running the Real Experts Series. No matter how good AI gets, it can't replace what a veteran knows. It's a 20 to 30 minute interview about what you've learned.

All it takes is a yes, and the three questions head your way. If you're slammed right now, that's fair.

Dana"""),
F2_FU=("the confident answer","Hey Mike, a no start can be a battery, a relay or a bad ground, and the internet names all three with equal confidence. What's the first thing you touch?"))
out={}
for k,d in leads.items():
    out[k]={fw:{"subject":v[0],"body":v[1]} for fw,v in d.items()}
    for fw,v in d.items():
        print(k[:12],fw,len(v[1].split()))
json.dump(out,open("leads.json","w"),indent=2)
json.dump({"five-star-auto-care-mentor@example.invalid":{"company":"5 Star Auto Care","city":"Mentor"},
"millennium-transmission-akron@example.invalid":{"company":"Millennium Transmission & Auto Care","city":"Akron"},
"auto-service-experts-grove-city@example.invalid":{"company":"Auto Service Experts OH","city":"Grove City"}},open("packets.json","w"),indent=2)

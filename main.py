from mastodon import Mastodon
import wikipedia

f = open('settings.py', 'r')
exec(f.read(), globals())
f.close()

wikipedia.set_lang(wiki_lang)
page = wikipedia.page(wikipedia.random())
text = '%s\n\n%s' % (page.summary, page.url)

shorten_summary = page.summary
while len(text) > 500:
    print('CUT')
    shorten_summary = shorten_summary.rsplit('.', 1)[0]
    text = '%s\n\n%s' % (shorten_summary, page.url)
print(text)
print('length:', len(text))

masto = Mastodon(
    access_token = 'pytooter_usercred.secret',
    api_base_url = mastodon_url
)

masto.log_in(
    mastodon_email,
    mastodon_password,
    to_file = 'pytooter_usercred.secret'
)
masto.status_post(text, visibility='unlisted')

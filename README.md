# Penman

Penman is a plugin for the [Sublime Text][sublime-text] text editor that allows
users to write well-formatted prose in plain-text using a markup language called
WriteML.

Penman is under active development, and currently only supports syntax
highlighting for WriteML documents. Future enhancements will include: 'goto
anything' support, markup snippets/completion, and the ability to export WriteML
documents to other formats (i.e. HTML and DOCX).

# WriteML

WriteML is a lightweight markup language designed specifically for writing prose
(e.g. short stories, novellas, novels, etc). It includes markup for: denoting
different sections of a work (chapters, scenes, etc); denoting blocks of text
(paragraphs, verse, etc); and formatting inline text (emphasis, etc).

In addition, WriteML incorporates the [TOML config file format][toml-github] for
configuring a work's metadata (i.e. information about the work apart from the
prose itself).

The following is a quick-and-dirty primer on WriteML markup. Note that -- like
Penman itself -- WriteML is also under active development, with full
documentation and real example documents coming soon.

```
---
# This is a TOML configuration block
title             = "An Example WriteML Document"
author.name       = "Me I. Myself"
author.writing-as = "M.I. Self"
---

# chapter
# Optional Chapter Title Here
# Optional Chapter Subtitle Here

Sections are marked as above; section types include things like: "introduction",
"part", "chapter", etc.

---
# Note to self: be sure to let users know that they can use TOML comments to
# leave themselves notes while they write...
---

There are two ways to break-up scenes within a chapter: one hash-mark for a
'soft' scene break (usually rendered as a small margin of space between
paragraphs); and two hash-marks for a 'hard' (or 'ornamental') scene break
(usually rendered the same as a 'soft' scene break, but with a sequence of
repeated characters, or a small icon of some sort, centered within the space
between paragraphs).

#

You can emphasize and offset text, like so:

Later, when I walked into the break room, I could see that Dan was reading
today's edition of [oem][The City Tabloid]. So I said, "Dan, do you really have
to read [em][that] in here?" He just sneered at me and went back to reading.

There's also markup for denoting 'alternate voice', which is meant for things
like a character's inner thoughts or dreams, or the literal voice of a character
you cannot directly observe (like a deranged character's alternate personality).

[av][Damn,] I thought. [av][I oughta knock that smirk right offa Dan's stupid
face...]

Of course, I knew I never would; that's really not the type of person I am.

#

You can also include links in your text [link-id][like this].

---
[link-id]
web = "https://google.com/?search=testing"
---

And if you get [tk][stumped? stuck?] on something, but just want to keep writing
and come back to fix it later, you can insert a [tk] (either with or without an
accompanying note, both of which you've now seen perfectly fine examples of).

#

You can mark a block of individual lines like this:

As I approached the break room the next day, I could see the door was closed and
it had a sign hanging on it which read:

  | If you don't like what I read,
  | you can use the other break room!

And, similarly, you can mark blocks of lyrics/verse like this:

So I barged in and began to sing at the top of my lungs:

  || Dan is dumb
  || He's a big dumb dummy
  ||
  || If he doesn't like my song
  || He can run home to his mummy!

And that's when I got fired.

# about the author

I am a person whose other book you can buy here:

[link-my-other-book]

###

Three hash-marks mark The End of the prose. After them (here) you can put more
configuration blocks, as well as any free-form notes (like these) you like.

Note that the link "link-my-other-book" in the markup above doesn't have any
text associated with it -- in this case, the URL will be used as the text...

---
# Note that all top-level key/value pairs implicitly belong to a table called
# "document" -- or, you can explicitly declare that table, like so...

[document]
last-updated = 2020-04-01

# If you don't want to mix config blocks with your prose, all your metadata
# can go here after The End

[link-my-other-book]
web    = "https://my-web.site/?id=my-book"
kindle = "https://amazon.com/?id=my-book"
kobo   = "https://kobo.com/?id=my-book"
---

That's all folks! Thank you for reading!
```

[sublime-text]: https://www.sublimetext.com
[toml-github]: https://github.com/toml-lang/toml
from multi_rake import Rake

def extract(text, lang):
  rake = Rake(language_code=lang)
  keywords = rake.apply(text)

  return keywords
from transformers import BlenderbotSmallTokenizer, BlenderbotSmallForConditionalGeneration

# Save model in model folder
mname = 'facebook/blenderbot_small-90M'
BlenderbotSmallForConditionalGeneration.from_pretrained(mname).save_pretrained('./model')
BlenderbotSmallTokenizer.from_pretrained(mname).save_pretrained('./model')

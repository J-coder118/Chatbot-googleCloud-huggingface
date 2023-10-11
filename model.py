from transformers import BlenderbotSmallTokenizer, BlenderbotSmallForConditionalGeneration

class ChatModel:
    def __init__(self):
        """Initialize model and tokenizer."""
        self.model = BlenderbotSmallForConditionalGeneration.from_pretrained('./model')
        self.tokenizer = BlenderbotSmallTokenizer.from_pretrained('./model')

    def get_reply(self, user_query):
        """Given user input, make bot prediction.
        
        Input: "Hi there"
        Ourput: "Hi how are you?"
        """
        inputs = self.tokenizer([user_query], return_tensors='pt')
        reply_ids = self.model.generate(**inputs)
        bot_answer = self.tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]
        return bot_answer

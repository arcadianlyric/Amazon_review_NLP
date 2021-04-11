from .base import BaseModel


class ReviewModel(BaseModel):
    def __init__(self):
        super().__init__()#py3, BaselModel is a class, so using orm multiple inheritance 'super'

        self.load_model('models/mnb_model.pkl')
        self.load_vec('models/tf_vec.pkl')

    def predict(self, line, highlight=True):
        sentiment = super(ReviewModel, self).predict(line)# inheritance predict() from basemodel ?

        # highlight words
        if highlight:
            highlight_word = [w for w in self.preprocessing(line).split()
                               if super(ReviewModel, self).predict(w) == sentiment]
            return sentiment, highlight_word
        else:
            return sentiment

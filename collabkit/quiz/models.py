from django.db import models


class Set(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)

    def __unicode__(self):
        return self.name

    def as_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Question(models.Model):
    set = models.ForeignKey(Set)
    name = models.TextField(max_length=500, blank=False, null=False)
    type = models.CharField(max_length=20, blank=False, null=False, choices=(
        ('tf', 'True or False'),
        ('mcq', 'Multiple Choice'),
        ('sa', 'Short Answer'),
        ('fb', 'Fill in the blanks')
    ))
    tf_answer = models.BooleanField(default=False)
    given_answer = models.TextField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (self.name, self.type)

    def check_tf(self, choice):
        return self.tf_answer == (int(choice) == 1)

    def check_mcq(self, answer_id):
        return len(QuestionAnswerChoice.objects.filter(question=self, pk=answer_id, answer=True)) == 1

    def check_fb(self, answer):
        return self.given_answer.strip() == answer.strip()

    def as_json(self):
        return {
            'id': self.id,
            'set': self.set.id,
            'name': self.name,
            'type': self.type,
            'tf_answer': self.tf_answer,
            'given_answer': self.given_answer,
            'choices': [question_answer.as_json() for question_answer in QuestionAnswerChoice.objects.filter(question=self)]
        }


class QuestionAnswerChoice(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    answer = models.BooleanField(default=False)
    question = models.ForeignKey(Question)

    def __unicode__(self):
        return '%s %s' % (self.name, self.answer)

    def as_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'answer': self.answer
        }
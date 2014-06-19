var app = angular.module('collabApp', []);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    $version = '0.1';
});

app.service('CollabService', ['$http', function($http){
    this.getSets = function () {
        return $http.get('/set/list');
    };

    this.getQuestions = function () {
        return $http.get('/question/list');
    };

    this.checkAnswerMCQ = function (questionId, answer) {
        return $http.get('/question/check_mcq', {
            questionId: questionId,
            answer: answer
        });
    };

    this.checkAnswerFB = function (questionId, answer) {
        return $http.get('/question/check_fb', {
            questionId: questionId,
            answer: answer
        });
    };

    this.checkAnswerTF = function (questionId, answer) {
        return $http.get('/question/check_tf', {
            questionId: questionId,
            answer: answer
        });
    };

    this.getAnswer = function (questionId, answer) {
        return $http.get('/question/get_answer', {questionId: question});
    };

}]);

app.controller('MainController', ['$scope', 'CollabService', function ($scope, CollabService) {
    $scope.version = '0.1';
    $scope.setselected = 1;

    $scope.question_answer = {};
    $scope.questions_correct = 0;
    $scope.questions_attempted = 0;

    $scope.init = function () {
        CollabService.getSets()
            .success(function (data) {
                $scope.sets = data.data;
            })
            .error(function (err) {
                console.log(err);
            });
        CollabService.getQuestions()
            .success(function (data) {
                $scope.questions = data.data;
            })
            .error(function (err) {
                console.log(err);
            });
    };

    $scope.showQuestions = function (setId) {
        $scope.setselected = setId;
    };

    $scope.answer = function (questionId, answerId, showAnswer) {
        showAnswer = typeof showAnswer !== 'undefined';
        var ans = $('#' + answerId);
        var val = ans.val();
        for(var i = 0 ; i < $scope.questions.length ; i++)
        {
            if($scope.questions[i].id === questionId)
            {
                var q = $scope.questions[i];
                if (q.type === 'mcq')
                {
                    var choices = q.choices;
                    for(var j = 0 ; j < choices.length ; j ++)
                    {
                        if(!showAnswer)
                        {
                            if (choices[j].id == val)
                            {
                                $scope.question_answer[questionId] = choices[j].answer;
                            }
                        }
                        else
                        {
                            if(choices[j].answer)
                            {
                                $(answerId).prop('checked', true);
                                $scope.question_answer[questionId] = true;
                            }
                        }


                    }
                }
                else if (q.type === 'tf')
                {
                    if(!showAnswer)
                    {
                        $scope.question_answer[questionId] = q.tf_answer === (val == 1);
                    }
                    else
                    {
                       $(answerId).prop('checked', true);
                       $scope.question_answer[questionId] = true;
                    }

                }
                else if (q.type === 'fb')
                {
                    if(!showAnswer)
                    {
                        $scope.question_answer[questionId] = $.trim(val) == q.given_answer;
                    }
                    else
                    {
                        ans.val(q.given_answer);
                        $scope.question_answer[questionId] = true;
                    }

                }
                else if (q.type === 'sa')
                {
                    if(!showAnswer)
                    {
                        $scope.question_answer[questionId] = $.trim(val) == q.given_answer;
                    }
                    else
                    {
                        ans.html(' ').val(q.given_answer);
                        $scope.question_answer[questionId] = true;
                    }
                }
            }
        }
    };
}]);
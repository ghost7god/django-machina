# -*- coding: utf-8 -*-

# Standard library imports
# Third party imports
# Local application / specific library imports
from machina.apps.conversation.polls.abstract_models import AbstractTopicPoll
from machina.apps.conversation.polls.abstract_models import AbstractTopicPollOption
from machina.apps.conversation.polls.abstract_models import AbstractTopicPollVote


class TopicPoll(AbstractTopicPoll):
    pass


class TopicPollOption(AbstractTopicPollOption):
    pass


class TopicPollVote(AbstractTopicPollVote):
    pass

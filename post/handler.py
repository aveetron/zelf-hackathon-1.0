
class SocialMediaPostHandler:

    def __init__(self):
        pass

    @staticmethod
    def post_handler(post_list) -> None:
        """
        if the authors were not added, then CollectContent
        will call this handler
        - now those auther_list will be handled by a
        serverless framework agent
        - serverless framework handles AWS SQS, Lambda in a
        hood
        - need to provide database cred using ssm


        :param author_response:
        :return: None
        """

    @staticmethod
    def auther_handler(auther_list) -> None:
        """
        if the authors were not added, then CollectContent
        will call this handler
        - now those auther_list will be handled by a
        serverless framework agent
        - serverless framework handles AWS SQS, Lambda in a
        hood


        :param author_response:
        :return: None
        """
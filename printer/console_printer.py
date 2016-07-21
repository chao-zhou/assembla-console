from global_info import GLOBAL_INFO
from local_datetime import to_local_time, is_today_local


def print_tickets(tickets):
    for ticket in tickets:
        print_ticket(ticket)


def print_header():
    print 'summary,user,status,updated'


def print_ticket(ticket):
    print u'#{0} - {1}'.format(ticket['number'], ticket['summary'])
    print u'     [user:{2}], [status:{0}], [updated at:{1}]'\
        .format(ticket['status'], to_local_time(ticket['updated_at']), get_user_name(ticket))


def get_user_name(ticket):
    user_ids = map(lambda u: u['id'], GLOBAL_INFO.swat_users)
    for comment in ticket.cached_comments:
        comment_updated_at = comment['updated_at']
        if comment['user_id'] in user_ids and is_today_local(comment_updated_at):
            user = filter(lambda u: u['id'] == comment['user_id'], GLOBAL_INFO.swat_users)[0]
            return user['name']
    return 'Unknown'
from global_info import GLOBAL_INFO
from local_datetime import is_today_local
from printer.csv_printer import print_tickets


def main():
    GLOBAL_INFO.load()

    swat_user_ids = map(lambda u: u['id'], GLOBAL_INFO.swat_users)
    commented_filter = lambda t: is_today_commented_ticket(t, swat_user_ids)
    modified_tickets = filter(commented_filter, GLOBAL_INFO.seismic_tickets)

    print_tickets(modified_tickets)
    print 'EOF'


def get_comments(ticket):
    comments = ticket.comments()
    ticket.cached_comments = comments
    return comments


def is_today_commented_ticket(ticket, user_ids):
    ticket_update_at = ticket['updated_at']
    if not is_today_local(ticket_update_at):
        return 0

    for comment in get_comments(ticket):
        comment_updated_at = comment['updated_at']
        if comment['user_id'] in user_ids and is_today_local(comment_updated_at):
            return 1
    return 0


if __name__ == "__main__":
    main()

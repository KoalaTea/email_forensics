from forensics import main

input('Testing valid slack email')
main('personal_test_emails/forwarded_slack_email.txt')
input('Testing an email that uses neither spf nor dkim')
main('personal_test_emails/picture_sent_from_my_phone.txt')
input('Testing an email with a domain being searched for that has no record')
main('personal_test_emails/random_rit_email.txt')
input('Testing an email that has a mismatch of dkim signature')
main('personal_test_emails/editedemail.txt')
input('Testing an email with bad headers')
main('personal_test_emails/bad_email_test.txt')

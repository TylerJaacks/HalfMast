from halfmast.half_staff_scrapper import HalfStaffScrapper


def lambda_handler(event, context):
    half_staff_scrapper = HalfStaffScrapper()

    half_staff_scrapper.get_soup()

    date = half_staff_scrapper.get_date()

    date_str = "{}-{}-{}".format(date[2], date[1], date[0])

    post_title = half_staff_scrapper.get_post_title()
    post_content = half_staff_scrapper.get_post_content()

    return {
        'date': date,
        'post_title': post_title,
        'post_content': post_content
    }


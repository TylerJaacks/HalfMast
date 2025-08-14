from halfmast.half_staff_scrapper import HalfStaffScrapper


def test_scrapper():
    scrapper = HalfStaffScrapper("https://halfstaff.org/")

    scrapper.get_soup()

    print(scrapper.get_date())
    print(scrapper.get_post_title())
    print(scrapper.get_post_content())

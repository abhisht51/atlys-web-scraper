from .dental_scraper import DentalStallScraper
from ..core.config import settings
from ..settings.json_storage import JSONStorage


class ScraperFactory:
    @staticmethod
    def get_scraper(scraper_type: str, storage_type: str, num_pages: int, proxy: str):
        if storage_type == "json":
            storage = JSONStorage()
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")

        if scraper_type == "dental_stall":
            return DentalStallScraper(
                num_pages=num_pages,
                proxy=proxy,
                storage=storage,
            )
        else:
            raise ValueError(f"Unknown scraper type: {scraper_type}")

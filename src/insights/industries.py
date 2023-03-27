from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    unique_industries = set()

    for job in data:
        if (job["industry"] != ''):
            unique_industries.add(job["industry"])

    return unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    result = []
    for job in jobs:
        if job['industry'] == industry:
            result.append(job)

    return result

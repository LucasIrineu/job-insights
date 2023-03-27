from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding='utf-8') as file:
        job_reader = csv.DictReader(file)
        result = [row for row in job_reader]
        return result


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    unique_jobs = set()
    for job in data:
        unique_jobs.add(job["job_type"])
    return unique_jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError

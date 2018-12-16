from common.bookupdateinfo import BookUpdateInfo
import argparse
import json
from pprint import pprint
from jinja2 import Template, Environment, FileSystemLoader
from datetime import datetime, date, timedelta
import os

class DigestParams:

    def __init__(self):
        self.isVerbose = False
        self.newWorksUrl = ''
        self.booksListUrl = ''
        self.newWorksFile = ''
        self.digestTemplatePath = ''
        self.digestOutputPath = ''

    @staticmethod
    def create(opts):
        result = DigestParams()

        result.isVerbose = opts.verbose
        result.newWorksUrl = opts.new_works_url
        result.booksListUrl = opts.books_list_url
        result.newWorksFile = opts.new_works_file
        result.digestTemplatePath = opts.digest_template
        result.digestOutputPath = opts.digest_file

        return result

class DigestBuilder:

    @staticmethod
    def loadNewBooksFromFile(fileName: str, verbose: bool):

        with open(fileName, encoding='utf-8') as f:
            data = json.load(f)

        result = []
        for w in data:
            updateInfo = BookUpdateInfo.createFromJson(w)
            if verbose:
                pprint(w)

            result.append(updateInfo)

        return result

    @staticmethod
    def buildDigest(params: DigestParams):
        if params.isVerbose:
            print("Generating digest '{digestFile}' from the template {digestTemplate} and '{newWorks}' as an updated books source:".format(digestFile=params.digestOutputPath,
                                                                                                                digestTemplate=params.digestTemplatePath,
                                                                                                                newWorks=params.newWorksFile))

        loader = FileSystemLoader(os.path.dirname(__file__) + '/templates')
        env = Environment(loader=loader)
        newBooks = DigestBuilder.loadNewBooksFromFile(params.newWorksFile, params.isVerbose)

        tpl = env.get_template(params.digestTemplatePath)
        result = tpl.render(newBooks=newBooks, currentDate=date.today(), fromDate=date.today() - timedelta(days=7))
        if params.isVerbose:
            print (result)

        fout = open(params.digestOutputPath, 'wt', encoding='utf-8')
        fout.write(result + '\n')
        fout.close()

    @staticmethod
    def main():
        parser = argparse.ArgumentParser(
            description='Generate digest for Author.Today portal news and updates.',
            epilog="""""",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        parser.add_argument(
            '-v', '--verbose',
            action='store_true',
            default=True,
            help='report what is generated')

        parser.add_argument(
            '--new-works-url',
            metavar='new_works_url',
            type=str,
            default='',
            help='URL of the updated works list page')

        parser.add_argument(
            '--books-list-url',
            metavar='books_url',
            type=str,
            default='',
            help='URL of the all books list page')

        parser.add_argument(
            '--new-works-file',
            metavar='new_works_file',
            type=str,
            default='',
            help='Path to JSON file with the updated works list')

        parser.add_argument(
            '--digest-file',
            metavar='file_file',
            type=str,
            default='',
            help='Path to the output digest file')

        parser.add_argument(
            '--digest-template',
            metavar='file_file',
            type=str,
            default='weekly_digest.md',
            help='Path to the digest template file')

        opt = parser.parse_args()
        params = DigestParams.create(opt)
        DigestBuilder.buildDigest(params)

if __name__ == "__main__":
    DigestBuilder.main()

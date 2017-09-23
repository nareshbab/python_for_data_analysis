import luigi


class PrintNumbers(luigi.Task):
    def requires(self):
        return []

    def output(self):
        return luigi.LocalTarget("numbers_up_to_10.txt")

    def run(self):
        with self.output().open('w') as f:
            for i in range(1, 11):
                f.write("{}\n".format(i))


class SquaredNumbers(luigi.Task):
    n = luigi.IntParameter()

    def requires(self):
        return [PrintNumbers(n=self.n)]

    def output(self):
        return luigi.LocalTarget("squares_up_to_{}.txt".format(self.n))

    def run(self):
        with self.input()[0].open() as fin, self.output().open('w') as fout:
            for line in fin:
                n = int(line.strip())
                out = n * n
                fout.write("{}:{}\n".format(n, out))
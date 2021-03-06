import sys


if (sys.version_info.major == 3):
    from gpudb.gpudb import GPUdb
    from gpudb.gpudb import GPUdbException
    from gpudb.gpudb import GPUdbRecordColumn
    from gpudb.gpudb import GPUdbRecordType
    from gpudb.gpudb import GPUdbRecord
    from gpudb.gpudb import GPUdbColumnProperty
    from gpudb.gpudb import GPUdbTable
    from gpudb.gpudb import GPUdbTableIterator
    from gpudb.gpudb import GPUdbTableOptions

    from gpudb.gpudb_ingestor import GPUdbWorkerList, GPUdbIngestor, InsertionException

    from gpudb.gpudb import collections
else:
    from gpudb import GPUdb
    from gpudb import GPUdbException
    from gpudb import GPUdbRecordColumn
    from gpudb import GPUdbRecordType
    from gpudb import GPUdbRecord
    from gpudb import GPUdbColumnProperty
    from gpudb import GPUdbTable
    from gpudb import GPUdbTableIterator
    from gpudb import GPUdbTableOptions

    from gpudb_ingestor import GPUdbWorkerList, GPUdbIngestor, InsertionException

    from gpudb import collections

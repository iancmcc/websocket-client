#include <Python.h>
#include <stdlib.h>

static PyObject * mask(PyObject* self, PyObject* args) {

    const char* mask;
    char* data;
    Py_ssize_t dcount;
    Py_ssize_t mcount;
    PyObject* result;
    int i;

    if (!PyArg_ParseTuple(args, "s#s#", &mask, &mcount, &data, &dcount)) {
        return NULL;
    }

    for(i=0; i<dcount; i++) {
        data[i] ^= mask[i % mcount];
    }

    result = Py_BuildValue("s#", data, dcount);
    return result;
}

static PyMethodDef MaskMethods[] = {
    {"mask",  mask, METH_VARARGS,
     "Mask a string."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC init_fastmask(void) {
        (void) Py_InitModule("_fastmask", MaskMethods);
}


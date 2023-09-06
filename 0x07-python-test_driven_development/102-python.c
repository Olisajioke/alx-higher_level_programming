#include <Python.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */

void print_python_string(PyObject *p)
{
	if (PyUnicode_Check(p))
	{
	PyObject *str = PyUnicode_AsUTF8String(p);

	if (str != NULL)
	{
		printf("String: %s\n", PyBytes_AsString(str));
		Py_DECREF(str);
	}
	else
	{
		PyErr_Print();
	}
	}
	else
	{
	PyErr_Print();
	}
}

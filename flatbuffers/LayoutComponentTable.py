# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers

class LayoutComponentTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsLayoutComponentTable(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LayoutComponentTable()
        x.Init(buf, n + offset)
        return x

    # LayoutComponentTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # LayoutComponentTable
    def PositionXPercentEnabled(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # LayoutComponentTable
    def PositionYPercentEnabled(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # LayoutComponentTable
    def PositionXPercent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # LayoutComponentTable
    def PositionYPercent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # LayoutComponentTable
    def SizeXPercentEnable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # LayoutComponentTable
    def SizeYPercentEnable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # LayoutComponentTable
    def SizeXPercent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # LayoutComponentTable
    def SizeYPercent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # LayoutComponentTable
    def StretchHorizontalEnabled(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # LayoutComponentTable
    def StretchVerticalEnabled(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # LayoutComponentTable
    def HorizontalEdge(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LayoutComponentTable
    def VerticalEdge(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LayoutComponentTable
    def LeftMargin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # LayoutComponentTable
    def RightMargin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # LayoutComponentTable
    def TopMargin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # LayoutComponentTable
    def BottomMargin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def LayoutComponentTableStart(builder): builder.StartObject(16)
def LayoutComponentTableAddPositionXPercentEnabled(builder, positionXPercentEnabled): builder.PrependBoolSlot(0, positionXPercentEnabled, 0)
def LayoutComponentTableAddPositionYPercentEnabled(builder, positionYPercentEnabled): builder.PrependBoolSlot(1, positionYPercentEnabled, 0)
def LayoutComponentTableAddPositionXPercent(builder, positionXPercent): builder.PrependFloat32Slot(2, positionXPercent, 0.0)
def LayoutComponentTableAddPositionYPercent(builder, positionYPercent): builder.PrependFloat32Slot(3, positionYPercent, 0.0)
def LayoutComponentTableAddSizeXPercentEnable(builder, sizeXPercentEnable): builder.PrependBoolSlot(4, sizeXPercentEnable, 0)
def LayoutComponentTableAddSizeYPercentEnable(builder, sizeYPercentEnable): builder.PrependBoolSlot(5, sizeYPercentEnable, 0)
def LayoutComponentTableAddSizeXPercent(builder, sizeXPercent): builder.PrependFloat32Slot(6, sizeXPercent, 0.0)
def LayoutComponentTableAddSizeYPercent(builder, sizeYPercent): builder.PrependFloat32Slot(7, sizeYPercent, 0.0)
def LayoutComponentTableAddStretchHorizontalEnabled(builder, stretchHorizontalEnabled): builder.PrependBoolSlot(8, stretchHorizontalEnabled, 0)
def LayoutComponentTableAddStretchVerticalEnabled(builder, stretchVerticalEnabled): builder.PrependBoolSlot(9, stretchVerticalEnabled, 0)
def LayoutComponentTableAddHorizontalEdge(builder, horizontalEdge): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(horizontalEdge), 0)
def LayoutComponentTableAddVerticalEdge(builder, verticalEdge): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(verticalEdge), 0)
def LayoutComponentTableAddLeftMargin(builder, leftMargin): builder.PrependFloat32Slot(12, leftMargin, 0.0)
def LayoutComponentTableAddRightMargin(builder, rightMargin): builder.PrependFloat32Slot(13, rightMargin, 0.0)
def LayoutComponentTableAddTopMargin(builder, topMargin): builder.PrependFloat32Slot(14, topMargin, 0.0)
def LayoutComponentTableAddBottomMargin(builder, bottomMargin): builder.PrependFloat32Slot(15, bottomMargin, 0.0)
def LayoutComponentTableEnd(builder): return builder.EndObject()

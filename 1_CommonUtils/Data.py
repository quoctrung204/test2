###test####
def data_getParseInfoNumberx2():
    return [{const_keyParentLevel(): const_relationSibling(),
             const_propType(): const_typeNumberx2PropertyWidget()}]

def data_getParseInfoNumber():
    return [{const_keyParentLevel(): const_relationSibling(),
             const_propType(): const_typeNumberPropertyWidget()}]
    
def data_getParseInfoNumberx3():
    return [{const_keyParentLevel(): const_relationSibling(),
             const_propType(): const_typeNumberx3PropertyWidget()}]

def data_getParseInfoNumberLineEdit():
    return [{const_keyParentLevel(): const_relationSibling(),
             const_propType(): const_typeNumberPropertyWidget()},
            {const_keyParentLevel(): const_relationChild(),
             const_propType(): const_typeCustomLineEditWidget()}]

def data_getParseInfoTextLineEdit():
    return [{const_keyParentLevel(): const_relationSibling(),
             const_propType(): const_typeTextPropertyWidget()},
            {const_keyParentLevel(): const_relationChild(),
             const_propType(): const_typeCustomLineEditWidget()}]
    
def data_getParseInfoFilenameLineEdit():
    return [{const_keyParentLevel(): const_relationSibling(),
             const_propType(): const_typeFilenamePropertyWidget()},
            {const_keyParentLevel(): const_relationChild(),
             const_propType(): const_typeCustomLineEditWidget()}]

def data_getParseInfoBoolButton():
    return [{const_keyParentLevel(): const_relationSibling(),
             const_propType(): const_typeBoolPropertyWidget()},
            {const_keyParentLevel(): const_relationChild(),
             const_propType(): const_typeCustomButtonWidget()}]

def data_getParseInfoEnumButton():
    return [{const_keyParentLevel(): const_relationSibling(),
             const_propType(): const_typeEnumPropertyWidget()},
            {const_keyParentLevel(): const_relationChild(),
             const_propType(): const_typeCustomButtonWidget()}]

def data_getParseInfoFilenameButton():
    return [{const_keyParentLevel(): const_relationSibling(),
             const_propType(): const_typeFilenamePropertyWidget()},
            {const_keyParentLevel(): const_relationChild(),
             const_propType(): const_typeCustomButtonWidget()}]
    
def data_getParseInfoColorButton():
    return [{const_keyParentLevel(): const_relationSibling(),
             const_propType(): const_typeColorPropertyWidget()},
            {const_keyParentLevel(): const_relationChild(),
             const_propType(): const_typeCustomButtonWidget(),
             const_propText(): "<...>"}]
    
def data_getParseInfoReferenceCombobox():
    return [{const_keyParentLevel(): const_relationSibling(),
             const_propType(): const_typeReferencePropertyWidget()},
            {const_keyParentLevel(): const_relationChild(),
             const_propType(): const_typeCustomComboBoxWidget()}]

def data_getParseInfoEnumCombobox():
    return [{const_keyParentLevel(): const_relationSibling(),
             const_propType(): const_typeEnumPropertyWidget()},
            {const_keyParentLevel(): const_relationChild(),
             const_propType(): const_typeCustomComboBoxWidget()}]
    
def data_getParseInfoByType(strType, lstProp=[]):
    mapFunc = {
               const_parseInfoNumberx2(): data_getParseInfoNumberx2,
               const_parseInfoNumber(): data_getParseInfoNumber,
               const_parseInfoNumberx3(): data_getParseInfoNumberx3,
               const_parseInfoNumberLineEdit(): data_getParseInfoNumberLineEdit,
               const_parseInfoTextLineEdit(): data_getParseInfoTextLineEdit,
               const_parseInfoFilenameLineEdit(): data_getParseInfoFilenameLineEdit,
               const_parseInfoBoolButton(): data_getParseInfoBoolButton,
               const_parseInfoEnumButton(): data_getParseInfoEnumButton,
               const_parseInfoFilenameButton(): data_getParseInfoFilenameButton,
               const_parseInfoColorButton(): data_getParseInfoColorButton,
               const_parseInfoReferenceCombobox(): data_getParseInfoReferenceCombobox,
               const_parseInfoEnumCombobox(): data_getParseInfoEnumCombobox}
    lstParseStep = mapFunc[strType]()
    i = 0
    for mapProp in lstProp:
        lstParseStep[i].update(mapProp)
        i += 1
    return lstParseStep

def data_getTabConfigData(strTabName): # mapLabelName, strParseInfoType, lstMapProp
    mtxInputTabDict = \
        {
        const_keyReferenceSurface():["'TargetSurveyVolume'",const_typeCustomComboBoxWidget()],
        const_keyXYUnitType() : ["'XYUnit*1000'", const_typeCustomButtonWidget() ],
        const_keyLinesToSkip():["'LinesToSkip*'",const_typeCustomLineEditWidget()],
        const_keyInline():["'Inline*Value'",const_typeCustomLineEditWidget()],
        const_keyCrossline():["'Crossline*'",const_typeCustomLineEditWidget()],
        const_keyEasting():["'Easting*'",const_typeCustomLineEditWidget()],
        const_keyNorthing():["'Northing*'",const_typeCustomLineEditWidget()],
        const_keyPetrelAddress(): ["'PetrelAddress'", const_typeCustomLineEditWidget()],
        const_keyPetrelPort(): ["'PetrelPort'", const_typeCustomLineEditWidget()],
        const_keyPetrelID(): ["'PetrelID'", const_typeCustomLineEditWidget()],
        const_keyReferenceID(): ["'ReferencePetrelID'", const_typeCustomLineEditWidget()],
        const_keyExportOption(): ["'.PetrelExport.'", const_typeCustomComboBoxWidget()],
        const_keyExportHorizonObject(): ["'.ExportHorizonObject.'", const_typeCustomComboBoxWidget()],
        const_keyAlphaScalerColorTable(): ["'.AlphaScalerTypeSelection.'", const_typeCustomComboBoxWidget()],
        const_keyActiveAttributes(): ["'ActiveAttributes'", const_typeCustomLineEditWidget()],
        const_keySurfaceUnit(): ["'SurfaceVerticalUnitOption'", const_typeCustomComboBoxWidget()],
        const_keySurfaceDepth(): ["'SurfaceVerticalDepthOption'", const_typeCustomComboBoxWidget()],
        # Horizon
        const_keySurveyReferenceVolume() : ["'*TargetVolume*'", const_typeCustomComboBoxWidget()],
        const_keyHorizonTimeOption() : ["'*HorizonZColumnTimeOption*'", const_typeCustomComboBoxWidget()],
        const_keyInlineColumn() : ["'*InlineColumn.*'", const_typeCustomLineEditWidget() ],
        const_keyCrosslineColumn() : ["'*CrosslineColumn.*'", const_typeCustomLineEditWidget() ],
        const_keyEastingColumn() : ["'.XColumn.'", const_typeCustomLineEditWidget() ],
        const_keyNorthingColumn() : ["'.YColumn.'", const_typeCustomLineEditWidget() ],
        const_keyTimeDepthColumn() : ["'.ZColumn.'", const_typeCustomLineEditWidget() ],
        const_keyFilePreview(): ["'TextHeaderWidget'",  const_typeTextHeaderWidget()],
        const_keyInvalidValue(): ["'*InvalidValue*Value*'", const_typeNumberPropertyWidget()],
        # Seismic
        const_keyXYUnit():["'.XYUnit.*.1000'",const_typeCustomButtonWidget()],
        const_keyZUnit():["'.ZUnit.'",const_typeCustomButtonWidget()],
        const_keyZUnitDropDown():["'ZUnit**'",const_typeCustomComboBoxWidget()],
        const_keyTimeDepth():["'.ZColumn.'",const_typeCustomLineEditWidget()],
        const_keyVelocitycolumn():["'.ParameterColumn.'",const_typeCustomLineEditWidget()],
        const_keyFunctionType():["'.columnTypeCombination.'",const_typeCustomComboBoxWidget()],
        const_keyPartialTemplateObject():["'*ActivePartialTemplateObject*'",const_typeCustomComboBoxWidget()],
        const_keyInlineBytePosition(): [hwO_mapInlineBytePositionLabel(), const_parseInfoNumberx2(), []],
        const_keyCrosslineBytePosition(): [hwO_mapCrosslineBytePositionLabel(), const_parseInfoNumberx2(), []],
        const_keyEastingBytePosition(): [hwO_mapEastingBytePositionLabel(), const_parseInfoNumberx2(), []],
        const_keyNorthingBytePosition(): [hwO_mapNorthingBytePositionLabel(), const_parseInfoNumberx2(), []],
        const_keySEGYSortOrder(): ["'IntParameterObject.SEGYSortOrder'", const_typeCustomComboBoxWidget()],
        const_keyActiveTrace(): ["'.ActiveTrace.'", const_typeCustomLineEditWidget()],
        const_keyTraceValue(): ["'.Trace*Value'", const_typeCustomLineEditWidget()],
        const_keyScaleBytePosition(): ["'Scale Byte Position '", const_typeNumberx2PropertyWidget()],
        const_keyScaleOverrideValue(): ["'ScaleOverrideValue*Value'", const_typeCustomLineEditWidget()],
        const_keyScaleOverrideValueLabel(): ["'*ScaleOverrideValue*Value*'", const_typeCustomLineEditWidget()],
        const_keyFirstMinILMinXLPair(): ["'IntVector2ParameterObject.IL_XL_0'", const_typeNumberx2PropertyWidget()],
        const_keyFirstXYPair(): ["'FloatVector2ParameterObject.COORDINATES_0'", const_typeNumberx2PropertyWidget()],
        const_keySecondMinILMaxXLPair(): ["'IntVector2ParameterObject.IL_XL_1'", const_typeNumberx2PropertyWidget()],
        const_keySecondXYPair(): ["'FloatVector2ParameterObject.COORDINATES_1'", const_typeNumberx2PropertyWidget()],
        const_keyThirdMaxILMaxXLPair(): ["'IntVector2ParameterObject.IL_XL_2'", const_typeNumberx2PropertyWidget()],
        const_keyThirdXYPair(): ["'FloatVector2ParameterObject.COORDINATES_2'", const_typeNumberx2PropertyWidget()],
        const_keyDeadTraceBytePosition(): ["'Dead Trace Byte Position '", const_typeNumberx2PropertyWidget()],
        const_keyDeadTraceSpecifierValue(): ["'Dead Trace Specifier Value '", const_typeNumberPropertyWidget()],
        const_keyAzimuth(): ["'AzimuthBytePosition*Value*X'", const_typeCustomLineEditWidget()],
        const_keyAzimuthReadoutPolicy(): ["'AzimuthReadoutPolicy*0'", const_typeCustomButtonWidget()],
        const_keySampleUnit(): ["'.SampleUnit'", const_typeCustomComboBoxWidget()],
        const_keyAttributeName(): ["'.AttributeName'", const_typeCustomComboBoxWidget()],
        const_keyAttributeUnit(): ["'.AttributeUnit'", const_typeCustomComboBoxWidget()],
        const_keyAttribute(): ["'Attribute'", const_typePairCombobox()],
        const_keyOffset(): ["'OffsetBytePosition'", const_typeNumberx2PropertyWidget()],
        const_keyInputObject0(): ["'.InputObject0'", const_typeCustomComboBoxWidget()],
        const_keyInputObject1(): ["'.InputObject1'", const_typeCustomComboBoxWidget()],
        const_keyInputFiles():["'.Filenames.'",const_typeCustomLineEditWidget() ],
        const_keyWiggleCount():["'.WiggleCount.'",const_typeCustomLineEditWidget() ],
        const_keyWigglePlotType():["'.WigglePlotType.'",const_typeCustomButtonWidget() ],
        const_keyTraceHeaderMathInline():["'.TraceHeaderMathInline.'",const_typeNumberx2PropertyWidget()],
        const_keyTraceHeaderMathCrossline():["'.TraceHeaderMathCrossline.'",const_typeNumberx2PropertyWidget()],
        const_keyTraceHeaderMathEasting():["'.TraceHeaderMathEasting.'",const_typeNumberx2PropertyWidget()],
        const_keyTraceHeaderMathNorthing():["'.TraceHeaderMathNorthing.'",const_typeNumberx2PropertyWidget()],
        const_keyTraceHeaderMathOffset():["'.TraceHeaderMathOffset.'",const_typeNumberx2PropertyWidget()],
        const_keyTraceHeaderMathAzimuth():["'.TraceHeaderMathAzimuth.'",const_typeNumberx2PropertyWidget()],
        const_keyCDPBytePosition():["'.CDPBytePosition'",const_typeNumberx2PropertyWidget()],
        # Well
        const_keyKBDepthDatum():["'DefaultDepthDatumToKellyBushing'",const_typeCustomButtonWidget()],
        const_keyNameColumn(): ["'.NameColumn'", const_typeCustomLineEditWidget()],
        const_keyKellyBushingColumn(): ["'KBColumn'", const_typeCustomLineEditWidget()],
        const_keyScaleFactorColumn(): ["'ParameterColumn'", const_typeCustomLineEditWidget()], # scale factor
        const_keyTotalMDColumn(): ["'TotalMDColumn'", const_typeCustomLineEditWidget()],
        const_keyVerticalDistanceUnit(): ["'VerticalDistanceUnit'", const_typeCustomButtonWidget()],
        const_keyMDColumn(): ["'MDColumn'", const_typeCustomLineEditWidget()],
        const_keyTVDSSColumn(): ["'TVDSSColumn'", const_typeCustomLineEditWidget()],
        const_keyTVDKBColumn(): ["'TVDKBColumn'", const_typeCustomLineEditWidget()],
        const_keyDxColumn(): ["'DxColumn'", const_typeCustomLineEditWidget()],
        const_keyDyColumn(): ["'DyColumn'", const_typeCustomLineEditWidget()],
        const_keyAzimuthColumn(): ["'AzimuthColumn'", const_typeCustomLineEditWidget()],
        const_keyInclinationColumn(): ["'InclinationColumn'", const_typeCustomLineEditWidget()],
        const_keyTimeUnit(): ["'TimeUnit'", const_typeCustomButtonWidget()],
        const_keyNegateDepthValues(): ["'NegateZ'", const_typeCustomButtonWidget()],
        const_keyDepthColumn(): ["'DepthColumn'", const_typeCustomLineEditWidget()],
        const_keyTimeColumn(): ["'TimeColumn'", const_typeCustomLineEditWidget()],
        const_keyDepthColumnType(): ["'DepthColumnType'", const_typeCustomComboBoxWidget()],
        const_keyDepthUnit(): ["'DepthUnit'", const_typeCustomButtonWidget()],
        const_keyWellNameColumn(): ["'.WellNameColumn'", const_typeCustomLineEditWidget()],
        const_keyTargetWellObject(): ["'TargetWellObject'", const_typeCustomComboBoxWidget()],
        const_keyColumnBreaks(): ["'ColumnBreaks'", const_typeCustomLineEditWidget()],
        # Angle mute and stacks
        const_keyPrestackObject_AMAS(): ["'.PrestackObject.'", const_typeCustomComboBoxWidget()],
        const_keyVelocityVolume_AMAS(): ["'.PoststackObject.'", const_typeCustomComboBoxWidget()],
        const_keyAngle_AMAS(): ["'.angle.'", const_typeCustomLineEditWidget()],
        const_keyILViz_AMAS(): ["'.Enabled.'", const_typeCustomButtonWidget()],
        # VF
        const_keyInterpolationMode(): ["'ActiveValueInterpolationMode'", const_typeCustomButtonWidget()]
        }
                    
    mtxParametersTabDict = \
        {
        const_keySampleSize():["'SampleSize'",const_typeNumberPropertyWidget()],
        const_keyInlineSize():["'InlineSize'",const_typeNumberPropertyWidget()],
        const_keyCrosslineSize():["'CrosslineSize'",const_typeNumberPropertyWidget()],
#         const_keySampleRange():["'SampleAnnotationRange'",const_typeNumberx2PropertyWidget()],
        #const_keyInlineRange():["'InlineAnnotationRange'",const_typeNumberx2PropertyWidget()],
        #const_keyCrosslineRange():["'CrosslineAnnotationRange'",const_typeNumberx2PropertyWidget()],
        #const_keyInlineStep():["'InlineAnnotationStep'",const_typeNumberPropertyWidget()],
        #const_keyCrosslineStep():["'CrosslineAnnotationStep'",const_typeNumberPropertyWidget()],
        #                          const_keyInlineRange():["'InlineRange.Value'",const_typeNumberx2PropertyWidget()],
        #                          const_keyCrosslineRange():["'CrosslineRange.Value'",const_typeNumberx2PropertyWidget()],
        const_keyInlineStep():["'InlineStride.Value'",const_typeNumberPropertyWidget()],
        const_keyCrosslineStep():["'CrosslineStride.Value'",const_typeNumberPropertyWidget()],
        const_keyInclusionDataRange():["'traceRange.Value'", const_typeNumberx2PropertyWidget()],
        const_keyPrimaryTrackingMethod():["'*Autotracker.PrimaryTrackingMethod*'", const_typeCustomButtonWidget()],
        const_keyInterpolation() : ["'InterpolationType'" , const_typeCustomComboBoxWidget()],
        const_keyInterpolateOverrideGriddingMode():["'OverrideGridding'", const_typeCustomButtonWidget()],
        const_keyAutotrackAlongGather():["'AutotrackAlongGather'", const_typeCustomButtonWidget()],
        const_keyFlatnessCutoff():["'FlatnessCutoff'", const_typeCustomLineEditWidget()],
        const_keyFillHolesHorizon():["'HorizonHoleFiller.IsFillerActive'", const_typeCustomButtonWidget()],
        const_keyIsWorkflowActive():["'IsWorkflowActive'", const_typeCustomButtonWidget()],
        # Horizon
        const_keySurveyReferenceVolume() : ["'.ReferenceVolume.'", const_typeCustomComboBoxWidget()],
        const_keySourceShape() : ["'.SourceShape.'", const_typeCustomComboBoxWidget()],
        const_keyMathConstantValue(): ["'*onstant*Value*'", const_typeCustomLineEditWidget()],
        const_keyMultipleIntersectionPolicy():["'.MultipleIntersectionPolicy.'", const_typeCustomButtonWidget()],
        const_keyLateralRangeMode():["'.LateralRangeMode.'", const_typeCustomButtonWidget()],
        const_keySpecifiedIntersection(): ["'.SpecifiedIntersection.'", const_typeCustomLineEditWidget()],
        const_keyValueCriteria():["'*Autotracker.DirectValueCriteria*'", const_typeCustomButtonWidget()],
        const_keyMergeMethod(): ["'*.MergeMethod.*'", const_typeCustomComboBoxWidget()],
        const_keyMergeOrder():["'*MergeOrder*'", const_typeCustomButtonWidget()],
        #                          const_keyInterpolation() : ["'*InterpolationType*'" , const_typeCustomComboBoxWidget()],
        const_keyResamplePerTraceChannels():["'*ResamplePerTraceChannels*'", const_typeCustomButtonWidget()],
        const_keyOverrideGridding():["'*OverrideGridding*'", const_typeCustomButtonWidget()],
        const_keyForceAnnotationCoordinates():["'*ForceAnnotationCoordinates*'", const_typeCustomButtonWidget()],
        const_keyInlineRange():["'*InlineRange*'", const_typeNumberx2PropertyWidget()],
        const_keyInlineStride():["'*InlineStride*'", const_typeCustomLineEditWidget()],
        const_keyCrosslineRange():["'*CrosslineRange*'", const_typeNumberx2PropertyWidget()],
        const_keyCrosslineStride():["'*CrosslineStride*'", const_typeCustomLineEditWidget()],
        const_keyTransposeLineAnnotations():["'*TransposeLineAnnotations*'", const_typeCustomButtonWidget()],
        const_keySizeDim0():["'*SizeDim0*'", const_typeCustomLineEditWidget()],
        const_keySizeDim1():["'*SizeDim1*'", const_typeCustomLineEditWidget()],
        const_keySizeDim2():["'*SizeDim2*'", const_typeCustomLineEditWidget()],
        # Seismic
        const_keyMinimumTime2D(): ["'TimeMin'" , const_typeCustomLineEditWidget()],
        const_keyMaximumTime2D(): ["'TimeMax'" , const_typeCustomLineEditWidget()],
        const_keyTimeIncrement2D(): ["'TimeStep'" , const_typeCustomLineEditWidget()],
        const_keyMinimumDepth2D(): ["'DepthMin'" , const_typeCustomLineEditWidget()],
        const_keyMaximumDepth2D(): ["'DepthMax'" , const_typeCustomLineEditWidget()],
        const_keyDepthIncrement2D(): ["'DepthStep'" , const_typeCustomLineEditWidget()],
        const_keySampleRange(): ["'.Sample*Range'", const_typeNumberx2PropertyWidget()],
        const_keySampleStep(): ["'.Sample*Step'", const_typeCustomLineEditWidget()],                                
        const_keyMaximumTime(): ["'maxTime'" , const_typeCustomLineEditWidget()],
        const_keyTimeIncrement(): ["'stepTime'", const_typeCustomLineEditWidget()],
        const_keyMinimumDepthInMeter(): ["'Minimum depth '" , const_typeNumberPropertyWidget()],
        const_keyMaximumDepthInMeter(): ["'maxDepth'" , const_typeCustomLineEditWidget()],
        const_keyDepthIncrementInMeter(): ["'stepDepth'", const_typeCustomLineEditWidget()],
        const_keyAutoEnableMute() : ["'Auto-enabled mute'", const_typeCustomButtonWidget()],
        const_keyOperation() : ["'.operation'", const_typeCustomComboBoxWidget()],
        const_keyTaperLength() : ["'Taper length'", const_typeNumberPropertyWidget()],
        const_keyNumberOfPairs(): ["'nPairs'", const_typeCustomLineEditWidget()],
        const_keyMute1() : ["'Offset1'" , const_typeCustomLineEditWidget()],
        const_keyTimet1() : ["'Time1'", const_typeCustomLineEditWidget()],
        const_keyMute2() : ["'Offset2'" , const_typeCustomLineEditWidget()],
        const_keyTimet2() : ["'Time2'", const_typeCustomLineEditWidget()],
        const_keyMute3() : ["'Offset3'" , const_typeCustomLineEditWidget()],
        const_keyTimet3() : ["'Time3'", const_typeCustomLineEditWidget()],
        const_keyMute4() : ["'Offset4'" , const_typeCustomLineEditWidget()],
        const_keyTimet4() : ["'Time4'", const_typeCustomLineEditWidget()],
        const_keyMute5() : ["'Offset5'" , const_typeCustomLineEditWidget()],
        const_keyTimet5() : ["'Time5'", const_typeCustomLineEditWidget()],
        const_keyMute6() : ["'Offset6'" , const_typeCustomLineEditWidget()],
        const_keyTimet6() : ["'Time6'", const_typeCustomLineEditWidget()],
        const_keyMute7() : ["Offset7'" , const_typeCustomLineEditWidget()],
        const_keyTimet7() : ["'Time7'", const_typeCustomLineEditWidget()],
        const_keyMute8() : ["'Offset8'" , const_typeCustomLineEditWidget()],
        const_keyTimet8() : ["'Time7'", const_typeCustomLineEditWidget()],
        const_keyMathOperation() : ["'Operation '", const_typeCustomComboBoxWidget()],
        const_keyButtonOperation() : ["'*peration*enumValue*'", const_typeCustomButtonWidget()],
        const_keyAzimuthRangeValue():["'.AzimuthRange2'", const_typeNumberx2PropertyWidget()],
        const_keyOffsetRange():["'FloatVector2ParameterObject.OffsetRange2'", const_typeNumberx2PropertyWidget()],
        const_keyOutputTraceCount():["'IntParameterObject.TraceCount2'", const_typeCustomLineEditWidget()],
        const_keyInputVelocityType():["'input_velocity_type'", const_typeCustomComboBoxWidget()],
        const_keyOutputVelocityType():["'output_velocity_type'", const_typeCustomComboBoxWidget()],
        const_keyXYUnitGoCAD(): ["'StringParameterObject.XYUnit'", const_typeCustomButtonWidget()],
        const_keyZUnitDropDown(): ["'ZUnit'", const_typeCustomComboBoxWidget()],
        const_keyUVWOrderGoCAD(): ["'IntParameterObject.UVWOrdering'", const_typeCustomComboBoxWidget()],
        const_keyAxisNU(): ["'IntParameterObject.AxisNU'", const_typeCustomLineEditWidget()],
        const_keyAxisNV(): ["'IntParameterObject.AxisNV'", const_typeCustomLineEditWidget()],
        const_keyAxisNW(): ["'IntParameterObject.AxisNW'", const_typeCustomLineEditWidget()],
        const_keyPropertyUnit(): ["'StringParameterObject.PropertyNonVelovityUnit'", const_typeCustomLineEditWidget()],
        const_keyVelocityUnit(): ["'PropertyVelocityUnit'", const_typeCustomButtonWidget()],
        const_keyVelocityScanMin(): ["'velocityScanMin*Value'", const_typeCustomLineEditWidget()],
        const_keyVelocityScanMax(): ["'velocityScanMax*Value'", const_typeCustomLineEditWidget()],
        const_keyVelocityScanStep(): ["'velocityScanStep*Value'", const_typeCustomLineEditWidget()],
        const_keyStretchFactor(): ["'stretchFactor*Value'", const_typeCustomLineEditWidget()],
        const_keyHalfWindowLength(): ["'halfWindowLength*Value'", const_typeCustomLineEditWidget()],
        const_keySampleUnit(): ["'StringParameterObject.SampleUnit.enumValue.*'", const_typeCustomComboBoxWidget()],
        const_keyAttributeName(): ["'StringParameterObject.AttributeName.enumValue.*'", const_typeCustomComboBoxWidget()],
        const_keyAttributeUnit(): ["'StringParameterObject.AttributeUnit.enumValue.*'", const_typeCustomComboBoxWidget()],
        const_keyAttribute(): ["'Attribute'", const_typePairCombobox()],
        const_keyAngleStart(): ["'firstAngle*Value'", const_typeCustomLineEditWidget()],
        const_keyAngleIncrement(): ["'angleInterval*Value'", const_typeCustomLineEditWidget()],
        const_keyAngleEnd(): ["'lastAngle*Value'", const_typeCustomLineEditWidget()],
        const_keyAngleMute(): ["'.angle*Value'", const_typeCustomLineEditWidget()],
        const_keyFrequencyMin(): ["'hzMin*Value'", const_typeCustomLineEditWidget()],
        const_keyFrequencyMax(): ["'hzMax*Value'", const_typeCustomLineEditWidget()],
        const_keyFrequencyStep(): ["'hzStep*Value'", const_typeCustomLineEditWidget()],
        const_keyVelocityFieldPercent(): ["'.percent*Value'", const_typeCustomLineEditWidget()],
        const_keyTraceValue(): ["'.Trace*Value'", const_typeCustomLineEditWidget()],
        const_keyOutputTypeParOfPeakPickAlg():["'.Output type.'", const_typeCustomComboBoxWidget()],
        const_keyNMOOperation():["'NMOOperation'", const_typeCustomComboBoxWidget()],
        const_keyAdjacentILGathers():["'*ILAdjacentGather*'", const_typeCustomLineEditWidget()],
        const_keyAdjacentXLGathers():["'*XLAdjacentGather*'", const_typeCustomLineEditWidget()],
        const_keyStackSupergather():["'*stackSupergather*'", const_typeCustomButtonWidget()],
        const_keyFilename():["'*.Filename.*'", const_typeCustomLineEditWidget()],
        # CSM
        const_keyVelocityAboveReferenceSurface() : ["'VelocityModel.WaterBottomVelocity'",const_typeCustomLineEditWidget()],
        const_keySliceInterval():["'VelocityModel.BoundaryInterval.'",const_typeCustomLineEditWidget()],
        const_keyLastSliceOffset(): ["'VelocityModel.LastBoundaryZ.'",const_typeCustomLineEditWidget()],
        const_keyVelocityValueRange(): ["'VelocityModel.ValueRange'",const_typeNumberx2PropertyWidget()],
        const_keyDepthValueRange(): ["'VelocityModel.DepthValueRange'",const_typeNumberx2PropertyWidget()],
        const_keyTimeValueRange(): ["'VelocityModel.TimeValueRange'",const_typeNumberx2PropertyWidget()],
        const_keyMisteValueRange(): ["'VelocityModel.MistieValueRange'",const_typeNumberx2PropertyWidget()],
        const_keyReplacementVelocityMap(): ["'VelocityModel.ReplacementVelocityMap'",const_typeCustomComboBoxWidget()],
        const_keyReplacementTimeDepthMap(): ["'VelocityModel.ReplacementTimeDepthMap'",const_typeCustomComboBoxWidget()],
        const_keySmoothingLength() : ["'VelocityModel.SmoothingLength.'",const_typeCustomLineEditWidget()],
        const_keyVerticalMax() : ["'VelocityModel.Prorate_VerticalMax'",const_typeCustomLineEditWidget()],
        const_keyVelocityMax() : ["'VelocityModel.Prorate_VelocityMax'",const_typeCustomLineEditWidget()],
        const_keyIncrement(): ["'VelocityModel.Prorate_Increment'",const_typeCustomLineEditWidget()],
        const_keyExtendType(): ["'VelocityModel.Prorate_Type'",const_typeCustomButtonWidget()],
        const_keyResetVisiblePerimeter(): ["'VelocityModel.ResetVisiblePerimeter'",const_typeCustomButtonWidget()],
        const_keyApplyVisiblePerimeter(): ["'VelocityModel.ApplyVisiblePerimeter'",const_typeCustomButtonWidget()],
        const_keyResetCornerPointPerimeter(): ["'VelocityModel.ResetCornerPointPerimeter'",const_typeCustomButtonWidget()],
        const_keyApplyCornerPointPerimeter(): ["'VelocityModel.ApplyCornerPointPerimeter'",const_typeCustomButtonWidget()],
        const_keySeismicReferenceDatumMode(): ["'VelocityModel.SeismicReferenceDatumMode'",const_typeCustomButtonWidget()],
        const_keyConstantEvaluation():["'VelocityModel.SeismicReferenceDatumConstant'",const_typeCustomLineEditWidget()],
        const_keyEvaluationMap(): ["'VelocityModel.SeismicReferenceDatum'",const_typeCustomComboBoxWidget()],
        const_keyCornerPoint0(): ["'VelocityModel.CornerPointOrigin'",const_typeNumberx2PropertyWidget()],                    
        const_keyCornerPoint1(): ["'VelocityModel.CornerPointMaxCrossline'",const_typeNumberx2PropertyWidget()],
        const_keyCornerPoint2(): ["'VelocityModel.CornerPointMaxInline'",const_typeNumberx2PropertyWidget()],
        const_keyExtendVerticalFunctions(): ["'VelocityModel.Prorate_ExtendEditableVerticalFunctions.'",const_typeCustomButtonWidget()],
        const_keySliceCount():["'VelocityModel.BoundaryCount.'", const_typeCustomLineEditWidget()],
        const_keyFirstSliceOffset():["'VelocityModel.FirstBoundaryOffset.'",const_typeCustomLineEditWidget()],
        const_keyConstantReplacementVelocity():["'VelocityModel.WaterBottomVelocity.'",const_typeCustomLineEditWidget()],
        const_keyReplacementVelocity():["'VelocityModel.ReplacementVelocityMode.'",const_typeCustomButtonWidget()],
        const_keyReferenceSurface():["'VelocityModel.ReferenceHorizon.'",const_typeCustomComboBoxWidget()],
        const_keyVelocityScaleFunction():["'VelocityModel.VelocityScalingFunction.'",const_typeCustomComboBoxWidget()],
        const_keyCorrectionMethod():["'VelocityModel.CorrectionMethod'",const_typeCustomButtonWidget()],
        const_keyVelocityPicks() :[ "'VelocityModel.VelocityPicks.'",const_typeCustomComboBoxWidget()],
        const_keyOutputAttribute() : ["'VelocityModel.OutputAttribute.'",const_typeCustomComboBoxWidget()],
        const_keyVMInlineStep(): ["'VelocityModel.InlineStep'", const_typeCustomLineEditWidget()],
        const_keyVMCrosslineStep(): ["'VelocityModel.CrosslineStep'", const_typeCustomLineEditWidget()],
        const_keyCopyInputDatumGriddingAndPerimeter(): ["'VelocityModel.ApplyDatumSurfacePerimeter'", const_typeCustomButtonWidget()],
        const_keySmoothingRadius():["'Radius'",const_typeCustomLineEditWidget()],
        # Angle mute and stacks
        const_keyILLocation_AMAS(): ["'.InlineLocation.'", const_typeCustomLineEditWidget()],
        const_keyXLLocation_AMAS(): ["'.CrosslineLocation.'", const_typeCustomLineEditWidget()]
        }

    mtxGeneralTabDict = \
        {
        const_keyVelocityPicks():["'VelocityModel.VelocityPicks'",const_typeCustomComboBoxWidget()],
        const_keyVelocityModel():["'VelocityModel.DisplayName'",const_typeCustomLineEditWidget()],
        const_keyValueSpace():["'ActiveValueSpace.'",const_typeCustomComboBoxWidget()],
        const_keyAttributeDimension():["'ActiveAttributeDimension.'",const_typeCustomComboBoxWidget()],
        const_keyPetrelID(): ["'PetrelID'", const_typeCustomLineEditWidget()],
        const_keyPetrelAddress(): ["'PetrelAddress'", const_typeCustomLineEditWidget()],
        const_keyPetrelPort(): ["'PetrelPort'", const_typeCustomLineEditWidget()],
        const_keyDisplayName(): [hwO_mapDisplayNameLabel(), const_parseInfoTextLineEdit(), []],
        # Seismic
        const_keyMeasureCode(): ["'.MeasureCode'", const_typeCustomComboBoxWidget()],
        const_keySampleRate(): ["'.OrgSampleRate'", const_typeCustomLineEditWidget()],
        const_keySampleRateScale(): ["'.SampleRateScale'", const_typeCustomLineEditWidget()],
        const_keySampleRateCalculated(): ["'.SampleRateCalculated'", const_typeCustomLineEditWidget()],
        const_keySamples(): ["'.Samples.'", const_typeCustomLineEditWidget()],
        const_keyAuthorityCode(): ["'.AuthorityCode.'", const_typeCustomLineEditWidget()],
        const_keyReferenceCRS(): ["'.ReferenceCRS.'", const_typeCustomLineEditWidget()],
        const_keyWKT(): ["'.WKT.'", const_typeCustomLineEditWidget()],
        }
        
    mtxBehaviorTabDict = \
        {
        #const_keyStart(): ["{Object:Exporter:RequestStartExport:DisplayName}", const_typeCustomButtonWidget()]
        const_keyStart(): ["'Exporter is running'", const_typeCustomButtonWidget()],
        const_keyExportIsNotRunning(): ["'Exporter is not running'", const_typeCustomLineEditWidget()],
        const_keyExportIsRunning(): ["'Exporter is running'", const_typeCustomLineEditWidget()],
        const_keyReadonly() : ["'IsObjectReadOnly.*.1'", const_typeCustomButtonWidget()],
        const_keyWhenExportComplete(): ["'AtExportCompleteMode'", const_typeCustomButtonWidget()],
        const_keyExportOptionColorTable(): ["'.ColorTableExportOption.'", const_typeCustomComboBoxWidget()],
        const_keyAlphaScaleExportOptionColorTable(): ["'.AlphaScaleExportOption.'", const_typeCustomComboBoxWidget()],
        const_keyOverallAlphaScale(): ["'.OverallAlphaScale.'", const_typeCustomLineEditWidget()],
        const_keyAttributeDimension():["'.VDSValueName.'",const_typeCustomLineEditWidget()],
        const_keyAttributeUnit():["'.VDSValueUnit.'",const_typeCustomLineEditWidget()],
        const_keyTargetValueDimension(): ["'.TargetValueDimension.'", const_typeCustomComboBoxWidget()],
        const_keySegmentsA():["'.SegmentA.'",const_typeCustomLineEditWidget()],
        const_keySegmentsB():["'.SegmentB.'",const_typeCustomLineEditWidget()],
        const_keyLocalPosition(): ["'.LocalPosition'", const_typeNumberx3PropertyWidget()],
        const_keyLocalOrientationX(): ["'.LocalOrientationX'", const_typeNumberx3PropertyWidget()],
        const_keyLocalOrientationY(): ["'.LocalOrientationY'", const_typeNumberx3PropertyWidget()],
        const_keyLocalOrientationZ(): ["'.LocalOrientationZ'", const_typeNumberx3PropertyWidget()],
        const_keyLocalScale(): ["'.LocalScale'", const_typeNumberx3PropertyWidget()],
        const_keyClosed(): ["'IsSurfaceClosed.*.1'", const_typeCustomButtonWidget()],
        const_keyReferenceObject(): ["'.ReferenceConstrainedVolumeObject.'", const_typeCustomComboBoxWidget()],
        const_keyAlternateReferencePosition():["'.ReferencePosition1.'",const_typeCustomLineEditWidget()],
        const_keyReferencePosition():["'.ReferencePosition0.'",const_typeCustomLineEditWidget()],
        const_keySliceBefore():["'.NeighborBefore.'",const_typeCustomLineEditWidget()],
        const_keySliceAfter():["'.NeighborAfter.'",const_typeCustomLineEditWidget()],
        const_keyOffsetStep():["'.Offset0.'",const_typeCustomLineEditWidget()],
        const_keyAlternateOffsetStep():["'.Offset1.'",const_typeCustomLineEditWidget()],
        const_keyAlternateDirection(): ["'.UseAlternateDirection.'", const_typeCustomButtonWidget()],
        # Horizon
        const_keyWorldOrigin(): ["'*WorldOrigin*'", const_typeNumberx2PropertyWidget()],
        const_keyInlineCount(): ["'*InlineSize*'", const_typeCustomLineEditWidget()],
        const_keyInlineAnnotationStep():["'*InlineAnnotationStep*'", const_typeCustomLineEditWidget()],
        const_keyInlineRangeFrom():["'*InlineAnnotationRange*X*'", const_typeCustomLineEditWidget()],
        const_keyInlineRangeTo():["'*InlineAnnotationRange*Y*'", const_typeCustomLineEditWidget()],
        const_keyCrosslineRangeFrom():["'*CrosslineAnnotationRange*X*'", const_typeCustomLineEditWidget()],
        const_keyCrosslineRangeTo():["'*CrosslineAnnotationRange*Y*'", const_typeCustomLineEditWidget()],
        const_keyCrosslineAnnotationStep():["'*CrosslineAnnotationStep*'", const_typeCustomLineEditWidget()],
        const_keyCrosslineCount(): ["'*CrosslineSize*'", const_typeCustomLineEditWidget()],
        const_keyInlineInterval(): ["'*.InlineInterval*'", const_typeCustomLineEditWidget()],
        const_keyCrosslineInterval(): ["'*.CrosslineInterval*'", const_typeCustomLineEditWidget()],
        const_keyCornerPoint0(): ["'*CornerPoint0*'", const_typeNumberx2PropertyWidget()],
        const_keyCornerPoint1(): ["'*CornerPoint1*'", const_typeNumberx2PropertyWidget()],
        const_keyCornerPoint2(): ["'*CornerPoint2*'", const_typeNumberx2PropertyWidget()],
        const_keyDisableCreationOfSurfaceAndPickObjects() : ["'*DisableAutomaticSurfaceAndPicks*'", const_typeCustomButtonWidget()],
        const_keyGeologicAge():["'*GeologicAge*'", const_typeCustomLineEditWidget()],
        const_keyActiveHorizonType() : ["'*ActiveHorizonType*'", const_typeCustomComboBoxWidget()],
        const_keyCorrespondingGeobodySurface() : ["'*CorrespondingGeobodySurface*'", const_typeCustomComboBoxWidget()],
        const_keyGeobodyGroup() : ["'*GeobodyGroup*'", const_typeCustomComboBoxWidget()],
        # Seismic
        const_keyInputShapeObject():["'.InputShapeObject.'", const_typeCustomComboBoxWidget()],
        const_keyLocalPositionX(): ["'.LocalPosition*X.'", const_typeCustomLineEditWidget()],
        const_keyLocalPositionY(): ["'.LocalPosition*Y.'", const_typeCustomLineEditWidget()],
        const_keyLocalPositionZ(): ["'.LocalPosition*Z.'", const_typeCustomLineEditWidget()],
        const_keyInlineLocation(): ["'.InlineLocation.'", const_typeCustomLineEditWidget()],
        const_keyCrosslineLocation(): ["'.CrosslineLocation.'", const_typeCustomLineEditWidget()],
        const_keyTraceLocation(): ["'.TraceLocation.'", const_typeCustomLineEditWidget()],
        const_keySampleLocation(): ["'.SampleLocation.'", const_typeCustomLineEditWidget()],
        const_keyInlineRange(): ["'.Inline*Range'", const_typeNumberx2PropertyWidget()],
        const_keyInlineStep(): ["'.Inline*Step'", const_typeCustomLineEditWidget()],
        const_keyCrosslineRange(): ["'.Crossline*Range'", const_typeNumberx2PropertyWidget()],
        const_keyCrosslineStep(): ["'.Crossline*Step'", const_typeCustomLineEditWidget()],
        const_keyCrosslineSpacing(): ["'.CrosslineSpacing'", const_typeNumberx2PropertyWidget()],
        const_keyInlineSpacing(): ["'.InlineSpacing'", const_typeNumberx2PropertyWidget()],    
        const_keyLatticeOrigin(): ["'.LatticeOrigin'", const_typeNumberx2PropertyWidget()],                                              
        const_keySampleRange(): ["'.Sample*Range'", const_typeNumberx2PropertyWidget()],
        const_keySampleStep(): ["'.SampleAnnotationStep'", const_typeCustomLineEditWidget()],
        const_keySampleCount(): ["'.SampleSize'", const_typeCustomLineEditWidget()],
        const_keyTraceRange(): ["'.TraceAnnotationRange'", const_typeNumberx2PropertyWidget()],
        const_keyTraceStep(): ["'.TraceAnnotationStep'", const_typeCustomLineEditWidget()],
        const_keyTraceCount(): ["'.TraceSize'", const_typeCustomLineEditWidget()],
        const_keyCDPRange(): ["'.BinAnnotationRange'", const_typeNumberx2PropertyWidget()],
        const_keyCDPStep(): ["'.BinAnnotationStep'", const_typeCustomLineEditWidget()],
        const_keyCDPCount(): ["'.BinSize'", const_typeCustomLineEditWidget()],
        const_keyCrosslineLength(): ["'.CrosslineLength'", const_typeCustomLineEditWidget()],
        const_keyInlineLength(): ["'.InlineLength'", const_typeCustomLineEditWidget()],
        const_keyCrosslineOrientation(): ["'.CrosslineOrientation'", const_typeCustomLineEditWidget()],
        const_keyInlineOrientation(): ["'.InlineOrientation'", const_typeCustomLineEditWidget()],
        const_keyWorldCrosslineStep(): ["'.WorldCrosslineSpacing'", const_typeNumberx2PropertyWidget()],
        const_keyWorldInlineStep(): ["'.WorldInlineSpacing'", const_typeNumberx2PropertyWidget()],
        const_keyAbsoluteVerticalRange(): ["'.AbsoluteVerticalRange'", const_typeNumberx2PropertyWidget()],
        const_keyRelativeVerticalRange(): ["'.RelativeVerticalRange'", const_typeNumberx2PropertyWidget()],                       
        const_keyVDSProduceStatus01():["'VDSProduceStatus01'", const_typeCustomComboBoxWidget()],
        const_keyVDSProduceStatus012():["'VDSProduceStatus012'", const_typeCustomComboBoxWidget()],
        const_keyVDSProduceStatus02():["'VDSProduceStatus02'", const_typeCustomComboBoxWidget()],
        const_keyVDSProduceStatus12():["'VDSProduceStatus12'", const_typeCustomComboBoxWidget()],
        const_keyVDSProduceStatus013():["'VDSProduceStatus013'", const_typeCustomComboBoxWidget()],
        const_keyVDSProduceStatus023():["'VDSProduceStatus023'", const_typeCustomComboBoxWidget()],
        const_keyVASMode(): ["'.VASMode*0'", const_typeCustomButtonWidget()],
        const_keyCloseSurface(): ["'.IsCloseSurface*0'", const_typeCustomButtonWidget()],
        const_keyStepDistance(): ["'.StepDistance.'", const_typeCustomLineEditWidget()],
        const_keyLineLocation(): ["'.LineLocation'", const_typeCustomLineEditWidget()],
        # Well
        const_keyActiveCheckshot(): ["'ActiveWellCheckshot'", const_typeCustomComboBoxWidget()],
        const_keyStopMeasuredDepth():["'MaxMD'",const_typeCustomLineEditWidget()],
        const_keyStartMeasuredDepth():["'MinMD'",const_typeCustomLineEditWidget()],
        const_keyUnit(): ["'.Unit.'", const_typeCustomLineEditWidget()],
        const_keyActivePath(): ["'*ActiveWellPath*'", const_typeCustomComboBoxWidget()],
        # TriangleSurface
        const_keyConstraintRegion(): ["'*InputRegion*'", const_typeCustomComboBoxWidget()],
        # Azimuth/Offset
        const_keyPrestackObject(): ["'*PrestackObject*'", const_typeCustomComboBoxWidget()]
        }
    
    mtxGeometryTabDict = \
        {
        const_keyVertexCount() : ["'VertexCount'", const_typeCustomLineEditWidget()],                     
        const_keyTriangleCount(): ["'TriangleCount'", const_typeCustomLineEditWidget()],
        const_keyVertices(): ["'Vertices'", const_typeNumberx3PropertyWidget()],
        # Well
        const_keyMDButton(): ["'WellPathGeometryTable*.1'", const_typeCustomTableHeadingWidget()],
        const_keyXButton(): ["'WellPathGeometryTable*.2'", const_typeCustomTableHeadingWidget()],
        const_keyYButton(): ["'WellPathGeometryTable*.3'", const_typeCustomTableHeadingWidget()],
        const_keyTVDKBButton(): ["'WellPathGeometryTable*.8'", const_typeCustomTableHeadingWidget()],
        const_keyTVDSSButton(): ["'WellPathGeometryTable*.9'", const_typeCustomTableHeadingWidget()]
        }
    
    mtxOutputTabDict = \
        {
        const_keyOverallCompleteFactor() : ["'OverallCompleteFactor'", const_typeCustomLineEditWidget()],
        const_keyHistogramScanning() : ["'HistogramCompleteFactor'", const_typeCustomLineEditWidget()],
        const_keyDatasetCompeleteFactor() : ["'DatasetCompleteFactor'", const_typeCustomLineEditWidget()],
        const_keyCacheToDisk(): ["'Prefetch.*.1'", const_typeCustomButtonWidget()],
        const_keyUnitOverallCompleteFactor() : [".OverallCompleteFactor'", const_typeCustomButtonWidget()],
        const_keyCompressionMethod(): ["'.CompressionMethod'", const_typeCustomButtonWidget()],
        const_keyCompressionMethodRelease2018(): ["'.CompressionMethod'", const_typeCustomComboBoxWidget()],
        const_keyBrowseExport() : ["'ExportFilename'", const_typeCustomButtonWidget()],
        const_keyBrowseCache() : ["'UserSpecifiedCacheFileName'", const_typeCustomButtonWidget()],
        const_keyStartExport() : ["'RequestStartExport'", const_typeCustomButtonWidget()],
        const_keyStopExport() : ["'RequestStopExport'", const_typeCustomButtonWidget()],
        const_keyValueRange() : ["'.ValueRange'", const_typeNumberx2PropertyWidget()],
        const_keyEstimatedValueRange() : ["'.EstimatedValueRange'", const_typeNumberx2PropertyWidget()],
        const_keyUserSpecifiedCachefileName():["'UserSpecifiedCacheFileName'",const_typeCustomLineEditWidget() ],
        const_keyPetrelInlineRange(): ["'OutputDim2Range'", const_typeNumberx2PropertyWidget()],
        const_keyPetrelCrosslineRange(): ["'OutputDim1Range'", const_typeNumberx2PropertyWidget()],
        const_keyPetrelTimeRange(): ["'OutputDim0Range'", const_typeNumberx2PropertyWidget()],
        const_keyPetrelInputInlineStep(): ["'InputDim2Step'", const_typeCustomLineEditWidget()],
        const_keyPetrelInputCrosslineStep(): ["'InputDim1Step'", const_typeCustomLineEditWidget()],
        const_keyPetrelInputTimeStep(): ["'InputDim0Step'", const_typeCustomLineEditWidget()],
        const_keyPetrelInputInlineRange(): ["'InputDim2Range'", const_typeNumberx2PropertyWidget()],
        const_keyPetrelInputCrosslineRange(): ["'InputDim1Range'", const_typeNumberx2PropertyWidget()],
        const_keyPetrelInputTimeRange(): ["'InputDim0Range'", const_typeNumberx2PropertyWidget()],
        const_keySampleRange(): ["'Sample*Range.'", const_typeNumberx2PropertyWidget()],
        const_keyOutputInlineRange(): ["'OutputInlineRange'", const_typeNumberx2PropertyWidget()],
        const_keyOutputCrosslineRange(): ["'OutputCrosslineRange'", const_typeNumberx2PropertyWidget()],
        const_keyExportShapeCRS(): ["'ExportShapeCRS'", const_typeCustomComboBoxWidget()],
        const_keyOverallCachingStatus(): ["'.PrefetchStatus.'", const_typeCustomLineEditWidget()],
        const_keyRealizeStatus(): ["'.DatasetCompleteStatus.'", const_typeCustomLineEditWidget()],
        const_keyReferenceShape(): ["'.ReferenceShape.'", const_typeCustomComboBoxWidget()],
        const_keyExportObject(): ["'ExportStackObject'", const_typeCustomComboBoxWidget()],
        const_keyExportPoststackObject(): ["'ExportPoststackObject'", const_typeCustomComboBoxWidget()],
        # Horizon
        const_keyValueRangeFrom() : ["'*.ValueRange*X*'", const_typeCustomLineEditWidget()],
        const_keyValueRangeTo() : ["'*.ValueRange*Y*'", const_typeCustomLineEditWidget()],
        const_keyEastingRange() : ["'*EastingRange*'", const_typeNumberx2PropertyWidget()],
        const_keyEastingRangeFrom() : ["'*EastingRange*X*'", const_typeCustomLineEditWidget()],
        const_keyEastingRangeTo() : ["'*EastingRange*Y*'", const_typeCustomLineEditWidget()],
        const_keyNorthingRange() : ["'*NorthingRange*'", const_typeNumberx2PropertyWidget()],
        const_keyNorthingRangeFrom() : ["'*NorthingRange*X*'", const_typeCustomLineEditWidget()],
        const_keyNorthingRangeTo() : ["'*NorthingRange*Y*'", const_typeCustomLineEditWidget()],
        const_keyXYUnitType() : ["'*XYUnit*1000*'", const_typeCustomButtonWidget() ],
        const_keyZUnitDropDown(): ["'*.ZUnitLengthType*1000*'", const_typeCustomButtonWidget()],
        const_keyExportHorizonObject(): ["'*.ExportHorizonObject.*'", const_typeCustomComboBoxWidget()],
        # Seismic
        const_keyCompressionPreviewMethod(): ["'.CompressionPreviewMode'", const_typeCustomComboBoxWidget()],                     
        const_keyCompressionTolerance(): ["'.CompressionTolerance.'", const_typeCustomLineEditWidget()],
        const_keyDataSize(): ["'.DataSize.'", const_typeCustomComboBoxWidget()],
        const_keySampleRangePhysical(): ["'.SampleRangePhysical'", const_typeNumberx2PropertyWidget()],
        const_keySampleStepPhysical(): ["'.SampleStepPhysical'", const_typeCustomLineEditWidget()],
        const_keyOffsetRangeLogical(): ["'.OffsetRangeLogical'", const_typeNumberx2PropertyWidget()],
        const_keyOffsetSpacingLogical(): ["'.OffsetSpacingLogical'", const_typeCustomLineEditWidget()],
        const_keyOffsetRangePhysical(): ["'.OffsetRangePhysical'", const_typeNumberx2PropertyWidget()],
        const_keyOffsetSpacingPhysical(): ["'.OffsetSpacingPhysical'", const_typeCustomLineEditWidget()],
        const_keyInlineRange(): ["'.InlineRange'", const_typeNumberx2PropertyWidget()],
        const_keyOutputSampleRange(): ["'.SampleIndexRange.'", const_typeNumberx2PropertyWidget()],
        const_keyOutputBinRange(): ["'OutputBinRange'", const_typeNumberx2PropertyWidget()],
        const_keyCrosslineRange(): ["'.CrosslineRange'", const_typeNumberx2PropertyWidget()],
        const_keyStartZ(): ["'.SampleOffset.Value'", const_typeCustomLineEditWidget()],
        const_keyInlineDecimation(): ["'.InlineDecimation'", const_typeCustomLineEditWidget()],
        const_keyCrosslineDecimation(): ["'.CrosslineDecimation'", const_typeCustomLineEditWidget()],
        const_keyTimeDepthRange(): ["'.SampleRangePhysical'", const_typeNumberx2PropertyWidget()],
        const_keyHistogramTracesToRead(): ["'.HistogramTracesToRead'", const_typeNumberPropertyWidget()],
        const_keyHistogramAutoscanEnabled(): ["'.HistogramAutoscanEnabled.*.1'", const_typeCustomButtonWidget()],
        const_keyAnalyzerStatus(): ["'AnalyzerStatus'", const_typeCustomLineEditWidget()],
        const_keyAzimuthRangeValue(): ["'AzimuthRange'", const_typeNumberx2PropertyWidget()],
        const_keyTraceNumberRangeValue(): ["'TraceNumberRange'", const_typeNumberx2PropertyWidget()],
        const_keyInlineSlicesFastAccess(): ["'.CacheDimensions01.'", const_typeCustomButtonWidget()],
        const_keyCrosslineSlicesFastAccess(): ["'.CacheDimensions02.'", const_typeCustomButtonWidget()],
        const_keySampleSlicesFastAccess(): ["'.CacheDimensions12.'", const_typeCustomButtonWidget()],
        const_keyVolumeFastAccess(): ["'.CacheDimensions012.'", const_typeCustomButtonWidget()],
        const_keyZUnit(): ["'*ZUnit*'", const_typeCustomButtonWidget()],
        const_keyExporterXYUnit(): ["'.XYUnit.'", const_typeCustomButtonWidget()],
        const_keyExporterAttributeUnit(): ["'.AttributeUnit.'", const_typeCustomButtonWidget()],
        const_keyOutputInlineRangeGoCAD(): ["'.inlineRange'", const_typeNumberx2PropertyWidget()],
        const_keyOutputCrosslineRangeGoCAD(): ["'.crosslineRange'", const_typeNumberx2PropertyWidget()],
        const_keyOutputSampleRangeGoCAD(): ["'.sampleIndexRange'", const_typeNumberx2PropertyWidget()],
        const_keyUseHistogramValueRangeGoCAD(): ["'.UseHistogramRange'", const_typeCustomButtonWidget()],
        const_keyCDPRange(): ["'.CDPRange.'", const_typeNumberx2PropertyWidget()],
        const_keyCreateNewTraceHeaders(): ["'CreateNewTraceHeaders'", const_typeCustomButtonWidget()]
        }

    mtxVisualizationTabDict = \
        {
        const_keyEnableVisualization() : ["'.Enabled*1'", const_typeCustomButtonWidget()],
        const_keyLineWeight():["'LineWeight.'",const_typeCustomLineEditWidget()],
        const_keyOverrideValueRange() : ["'Override value range'", const_typeNumberx2PropertyWidget()],
        const_keyValueRange() : ["'.ValueRange'", const_typeNumberx2PropertyWidget()],
        const_keyColorTable1() : ["'ColorTable1D1'", const_typeCustomComboBoxWidget()],
        const_keyDisplayContourAnnotations() : ["'*.ContourAnnotationSize'", const_typeCustomLineEditWidget()],
        const_keyVizScope3DWindow() : ["'.VolumeObject3DOrWindowScope*0'", const_typeCustomButtonWidget()],
        const_keyVizScopeHorizonWindow() : ["'.HorizonTypeObjectOrWindowScope*0'", const_typeCustomButtonWidget()],
        const_keyVizScopeVolumeSliceWindow() : ["'.VolumeSliceOrWindowScope*0'", const_typeCustomButtonWidget()],
        const_keyVizScopeLineWindow() : ["'.LineModelOrWindowScope*0'", const_typeCustomButtonWidget()],
        const_keyVizScopePointsetWindow() : ["'.LineModelOrWindowScope*0'", const_typeCustomButtonWidget()],                            
        const_keyVizScopeSurfaceWindow() : ["'.LineModelOrWindowScope*0'", const_typeCustomButtonWidget()],
        const_keyEnableBoundingBox() : ["'.BoundingBoxEnabled*1'", const_typeCustomButtonWidget()],
        const_keyReadoutMethod() : ["'*.DefaultReadoutMode.*'", const_typeCustomButtonWidget()],
        const_horizonAttribute1Viz() :["'TargetObject1'", const_typeCustomComboBoxWidget()],
        const_keyIntersectionRenderingEnabled() : ["'IntersectionRenderingEnabled'", const_typeCustomButtonWidget()],
        const_keyDefaultAttributeCount() : ["'DefaultAttributeCount'", const_typeCustomButtonWidget()],
        const_key3DRegion() : ["'DefaultRegion3D'", const_typeCustomComboBoxWidget()],
        const_keyBottomOffset() : ["'BottomOffset.Value'", const_typeCustomLineEditWidget()],
        const_keyInputObject1(): ["'InputObject1'", const_typeCustomComboBoxWidget()],
        # Horizon
        const_keyBlendingMode():["'RenderInstanceHorizonObject.ActiveCompositingMode'",const_typeCustomButtonWidget()],
        const_keyAttributes() : ["'ActiveAttributeCount'", const_typeCustomButtonWidget()],
        const_keyColor() : ["'Overall color'", const_typeColorPropertyWidget()],
        const_keyDisplayContours() : ["'*DisplayContours*1*'", const_typeCustomButtonWidget()],
        const_keyDisplayContourLinesEvery() : ["'*ContourIncrement*'", const_typeCustomLineEditWidget()],
        const_keyDisplayContourRangeFrom() : ["'*ContourRange*X*'", const_typeCustomLineEditWidget()],
        const_keyDisplayContourRangeTo() : ["'*ContourRange*Y*'", const_typeCustomLineEditWidget()],
        const_keyDisplayContourLinesBetween() : ["'Display contour lines between'", const_typeNumberx2PropertyWidget()],
        const_keyHorizonVisualizationMode() : ["'*HorizonRenderMode*0*'", const_typeCustomButtonWidget()],
        const_keyTargetPoststack(): ["'*TargetVolume*'", const_typeCustomComboBoxWidget()],
        const_keyTargetVolumeTransferFunction(): ["'*TransferFunction1D*'", const_typeCustomComboBoxWidget()],
        const_keyThicknessStart(): ["'*ThicknessStart*'", const_typeCustomLineEditWidget()],
        const_keyThicknessStop(): ["'*ThicknessStop*'", const_typeCustomLineEditWidget()],
        const_keyConstrainingHorizon() : ["'*TargetHorizon*'", const_typeCustomComboBoxWidget()],
        # Seismic
        const_keyAttribute1(): ["'TargetObject1.'", const_typeCustomComboBoxWidget()],
        const_keyAttribute2(): ["'*.TargetObject2*'", const_typeCustomComboBoxWidget()],
        const_keyAttribute3(): ["'*.TargetObject3*'", const_typeCustomComboBoxWidget()],
        const_keyValueCutoff(): ["'ValueCutoff'", const_typeCustomLineEditWidget()],
        const_keyOffsetScale(): ["'GatherScale'", const_typeCustomLineEditWidget()],
        const_keyDefaultSurfaceRenderingMode(): ["'.DefaultSurfaceRenderingMode'", const_typeCustomButtonWidget()],                    
        const_keyColorTable3D(): ["'ActiveTransferFunction3D'", const_typeCustomComboBoxWidget()],
        # Well
        const_keyDisplayModeWellPath(): ["'DefaultWellDisplacementMode'", const_typeCustomComboBoxWidget()],
        const_keyDisplayModeWellLog(): ["'DefaultLogDisplacementMode'", const_typeCustomComboBoxWidget()],
        const_keyRadius(): ["'DefaultWellRadius'", const_typeCustomLineEditWidget()],
        const_keyMarkerRadius(): ["'.Radius.'", const_typeCustomLineEditWidget()],
        const_keyThickness(): ["'.Thickness.'", const_typeCustomLineEditWidget()],
        const_keyLogRadius(): ["'.LogRadius.'", const_typeCustomLineEditWidget()],
        const_keyDisplayColor(): ["'.DisplayColor.'", const_typeColorPropertyWidget()],
        const_keyDefaultShowLocation(): ["'.DefaultShowLocation.'", const_typeCustomButtonWidget()],
        # CSM
        const_keyPointSize():["'.DefaultPointSize*'",const_typeCustomLineEditWidget() ]
        }
    
    mtx2wayVisualizationTabDict = \
        {
        const_keyEnableVisualization() : ["'RemoveTwoWayCoRendering'", const_typeCustomButtonWidget()],
        #Seismic
        const_keyBlendingMode(): ["*.ActiveCompositingMode.*", const_typeCustomButtonWidget()],
        const_keyRemoveTwoWayBlending() : ["'RemoveTwoWayCoRendering'", const_typeCustomButtonWidget()],
        const_keyRemoveThreeWayBlending():["'RemoveThreeWayCoRendering'", const_typeCustomButtonWidget()]
        }
    
    mtxLatticeTabDict = \
        {
        const_keyInlineInterval(): ["'.InlineInterval'", const_typeCustomLineEditWidget()],
        const_keyCrosslineInterval(): ["'.CrosslineInterval'", const_typeCustomLineEditWidget()],
        const_keyCornerPoint0(): ["'.CornerPoint0'", const_typeNumberx2PropertyWidget()],
        const_keyCornerPoint1(): ["'.CornerPoint1'", const_typeNumberx2PropertyWidget()],
        const_keyCornerPoint2(): ["'.CornerPoint2'", const_typeNumberx2PropertyWidget()],
        const_keyCrosslineLength(): ["'.CrosslineLength'", const_typeCustomLineEditWidget()],
        const_keyInlineLength(): ["'.InlineLength'", const_typeCustomLineEditWidget()],
        const_keyCrosslineOrientation(): ["'.CrosslineOrientation'", const_typeCustomLineEditWidget()],
        const_keyInlineOrientation(): ["'.InlineOrientation'", const_typeCustomLineEditWidget()],
        const_keyWorldCrosslineStep(): ["'.WorldCrosslineSpacing'", const_typeNumberx2PropertyWidget()],
        const_keyWorldInlineStep(): ["'.WorldInlineSpacing'", const_typeNumberx2PropertyWidget()],
        const_keyOrigin(): ["'.Origin'", const_typeNumberx2PropertyWidget()],
        const_keyInlineRange(): ["'.Inline*Range'", const_typeNumberx2PropertyWidget()],
        const_keyInlineSpacing(): ["'.InlineSpacing'", const_typeNumberx2PropertyWidget()],
        const_keyInlineStep(): ["'.Inline*Step'", const_typeCustomLineEditWidget()],
        const_keyCrosslineRange(): ["'.Crossline*Range'", const_typeNumberx2PropertyWidget()],
        const_keyCrosslineSpacing(): ["'.CrosslineSpacing'", const_typeNumberx2PropertyWidget()],
        const_keyCrosslineStep(): ["'.Crossline*Step'", const_typeCustomLineEditWidget()],
        const_keySampleRange(): ["'.Sample*Range'", const_typeNumberx2PropertyWidget()],
        const_keySampleStep(): ["'.Sample*Step'", const_typeCustomLineEditWidget()],
        const_keySetLatticeMethod() : ["'.SetLatticeMethod.'", const_typeCustomButtonWidget()],
        const_keyLatticeReference() : ["'.LatticeReference.'", const_typeCustomComboBoxWidget()],
        const_keyWorldOrigin():["'.WorldOrigin'", const_typeNumberx2PropertyWidget()],
        # Seismic
        const_keySetLatticeMethod() : ["'.SetLatticeMethod.'", const_typeCustomButtonWidget()],
        const_keyLatticeReference() : ["'.LatticeReference.'", const_typeCustomComboBoxWidget()],
        # Inva
        const_keyPrestackILXLIntervals():["'*.PrestackLatticeIntervalCount*'", const_typeNumberx2PropertyWidget()],
        const_keyPrestackILXLLengths():["'*PrestackLatticeStepLength*'", const_typeNumberx2PropertyWidget()],
        const_keyRoundILIntervals():["'*.SelectInlineIntervalCount.*'", const_typeCustomComboBoxWidget()],
        const_keyRoundXLIntervals():["'*.SelectCrosslineIntervalCount.*'", const_typeCustomComboBoxWidget()],
        const_keyEffectiveILIntervals():["'*.VerticalFunctionSetInlineCount.*'", const_typeCustomLineEditWidget()],
        const_keyEffectiveXLIntervals():["'*.VerticalFunctionSetCrosslineCount.*'", const_typeCustomLineEditWidget()],
        const_keyVFSetILXLLength():["'*.VerticalFunctionSetLatticeStepLength*'", const_typeNumberx2PropertyWidget()],
        const_keyInfiniteVoxel() : ["'.InfiniteVoxelResolution.'", const_typeCustomButtonWidget()],
        }

    mtxCRSTabDict = \
        {
        const_keyCRS() : ["'CRS'", const_typeCustomComboBoxWidget()],
        }
        
    mtxPlacementTabDict = \
        {
        # Well
        const_keyKellyBushing(): ["'KellyBushing'", const_typeCustomLineEditWidget()],
        const_keyLocationX(): ["'Location*X'", const_typeCustomLineEditWidget()],
        const_keyLocationY(): ["'Location*Y'", const_typeCustomLineEditWidget()],
        const_keyMeasuredDepth(): ["'MeasuredDepth'", const_typeCustomLineEditWidget()],
        const_keyUWI(): ["'UWI'", const_typeCustomLineEditWidget()],
        const_keyMistieValue(): ["'.MistieValue.'", const_typeCustomLineEditWidget()],
        const_keyOwningWell(): ["'*OwningWell*'", const_typeCustomComboBoxWidget()]
        }

    mtxDataTabDict = \
        {
        const_keyAzimuthHistogramTable(): ["'.AzimuthHistogramTable*'", const_typeCustomTableHeadingWidget()],
        # Well
        const_keyMDButton(): ["'.MDDataPreviewTable*'", const_typeCustomTableHeadingWidget()],
        const_keyCreateTWT(): ["'CreateTWT'", const_typeCustomLineEditWidget()],
        const_keyCreateDepth(): ["'CreateDepth'", const_typeCustomLineEditWidget()],
        const_keyTWTButton(): ["'.MDDataPreviewTable*.2'", const_typeCustomTableHeadingWidget()],
        const_keyTVDSSButton(): ["'.MDDataPreviewTable*.4'", const_typeCustomTableHeadingWidget()],
        const_keyCreateFullySpecifiedControlPoint(): ["'*CreateFullySpecifiedControlPoint*'", const_typeCustomButtonWidget()],
        # VF
        const_keyVFControlPoints(): ["'*Vertical*function*control*points*'", const_typeCustomObjectBrowserLineWidget()],
        }
    
    mtxAlgoParamTabDict = \
        {
        # Inva
        const_keyVelScanMin():["'*.velocityScanMin.*'", const_typeCustomLineEditWidget()],
        const_keyVelScanMax():["'*.velocityScanMax.*'", const_typeCustomLineEditWidget()],
        const_keyVelScanStep():["'*.velocityScanStep.*'", const_typeCustomLineEditWidget()],
        const_keyEtaExtent():["'*.etaScale.*'", const_typeNumberx2PropertyWidget()],
        const_keyEtaIncrementValue():["'*.etaScaleStep.*'", const_typeCustomLineEditWidget()],
        const_keyVelocityScaleFactor():["'*Float*.VelocityScale.*'", const_typeCustomLineEditWidget()],
        const_keyVelocityPercentagesRange():["'*velocityScale*'",const_typeNumberx2PropertyWidget()],
        const_keyVelocityPercentagesStep():["'*velocityScaleStep*'",const_typeCustomLineEditWidget()],
        const_keyStackTraceRange():["'*offsetRange*'",const_typeNumberx2PropertyWidget()],
        const_keyVelocityExtent(): ["'*.PercentageVelocityRange.*'", const_typeNumberx2PropertyWidget()],
        const_keyVelocityStep(): ["'*.PercentageVelocityStride.*'", const_typeCustomLineEditWidget()],
        const_keyAdjacentTraces(): ["'*.AdjacentTraces.*'", const_typeCustomLineEditWidget()],
        const_keyAdjacentTraceOption(): ["'*.AdjacentTraceOption.*'", const_typeCustomButtonWidget()],
        const_keyInclusionDataRange(): ["'*.offsetRange.*'", const_typeNumberx2PropertyWidget()]
        }
    
    mtxInputVizParamsDict = \
        {
        # Inva
        const_keyInputVF_InVA():["'*.CustomVerticalFunctionImport.*'",const_typeCustomComboBoxWidget()],
        const_keyInputGathers_InVA():["'*.PrestackObject.*'",const_typeCustomComboBoxWidget()],
#         const_keyViz_InVA():["'*.Enabled.*'",const_typeCustomButtonWidget()],
        const_keyILLocation_InVA():["'*.InlineLocation.*'",const_typeCustomLineEditWidget()],
        const_keyXLLocation_InVA(): ["'*.CrosslineLocation.*'", const_typeCustomLineEditWidget()],
        const_keyOverrideSectionViewRange_InVA(): ["'*.Section*.OverrideSectionPhysicalRange*'", const_typeNumberx2PropertyWidget()]
        }
    
    mtxInfoTabDict = \
        {
        const_keyDisplayObjectType():["'*DisplayObjectType*'", const_typeCustomLineEditWidget()],
        }

    if strTabName == const_tabInput():
        return mtxInputTabDict
    elif strTabName == const_tabParameters():
        return mtxParametersTabDict
    elif strTabName == const_tabBehavior():
        return mtxBehaviorTabDict
    elif strTabName == const_tabGeometry():
        return mtxGeometryTabDict
    elif strTabName == const_tabOutput():
        return mtxOutputTabDict
    elif strTabName == const_tabVisualization():
        return mtxVisualizationTabDict
    elif strTabName == const_tabGeneral(): 
        return mtxGeneralTabDict
    elif strTabName == const_tabLattice(): 
        return mtxLatticeTabDict
    elif strTabName == const_tabCRS(): 
        return mtxCRSTabDict
    elif strTabName == const_tabPlacement():
        return mtxPlacementTabDict
    elif strTabName == const_tabData():
        return mtxDataTabDict
    elif strTabName == const_tabAlgoParam():
        return mtxAlgoParamTabDict
    elif strTabName == const_inputVizParams():
        return mtxInputVizParamsDict
    elif strTabName == const_tabInfo():
        return mtxInfoTabDict
    elif strTabName == const_tabTwoWayVisualization():
        return mtx2wayVisualizationTabDict
    
def data_getDataFilePath(strFileName, strExtension, strDataset = ""):
    strPath =  "%s.%s" % (strFileName, strExtension)
    lstColorTable = ["Petrel_colortable", "Petrel_colortable_RWB", "Voxet_3", "Voxet_4"]
    lstSurface_models_SMF = ["Slope", "Crater", "Bunny"]
    lstSurface_model_SMF_EMVision = ["hor1_mod", "hor2_subtract1500"]
    lstLundinConvertedFiles_List = ["HG1_prestack", "HG2_prestack","HG3_prestack","HG4_prestack", "Stack_HG1", "Stack_HG2", "Stack_HG3", "Stack_HG4", "Vels_HG1", "Vels_HG2", "Vels_HG3", "Vels_HG4"]
    lstLundinList = ["HG1", "HG2", "HG3", "HG4", "HG1_4Inlines", "Stack_HG1", "Stack_HG2", "Stack_HG3", "Stack_HG4", "Vels_HG1", "Vels_HG2", "Vels_HG3", "Vels_HG4"]
    lstLundinList_Converted_SMS = ["HG1", "HG2", "HG3", "HG4", "HG1_4Inlines", "Stack_HG1_LOD3", "Vels_HG1", "HG1.vds_HG1.vds_Vels_HG1.vds_[Offset_to_Angle]_[AVO_Attributes]"]
    
    lstWAZList = ["WAZ_01-10",
               "WAZ_11-20",
               "WAZ_21-30",
               "WAZ_31-40",
               "WAZ_41-50",
               "WAZ_51-60",
               "WAZ_61-70",
               "WAZ_71-80",
               "WAZ_81-90",
               "WAZ_111-120",
               "WAZ_121-130",
               "WAZ_131-140",
               "WAZ_141-150",
               "WAZ_151-160",
               "WAZ_161-170",
               "WAZ_171-180",
               "WAZ_181-190",
               "WAZ_191-200",
               "WAZ_201-210",
               "WAZ_211-220",
               "WAZ_221-230",
               "WAZ_231-240",
               "WAZ_241-250",
               "WAZ_251-260",
               "WAZ_261-270",
               "WAZ_271-280",
               "WAZ_281-290",
               "WAZ_291-300",
               "WAZ_301-310",
               "WAZ_311-320",
               "WAZ_321-330",
               "WAZ_331-340",
               "WAZ_341-350",
               "WAZ_351-360"
                   ]
    lstEMVisionList = ["hor1", "hor2", "salt_top_resamp", "nsurf1", "nsurf2"]
    lstEMVision_SamplingHorizon_List = ["horB_sub", "horB_full", "vp_full", "vp_sub"]
    lstEMVision_405_voxet_List = ["region_mask"]
    lstEMVision_Mixed_Units_Manual = ["topography", "vel_p95_dx50.rsf_3D_gocad", "vel_p95_dx50.rsf_3D_gocadFt", "vel_p95_dx50.rsf_3D_gocadFtM","vel_p95_dx50.rsf_3D", "gather_vel_p95_az0_98","gather_vel_p95_az0_98Ft","gather_vel_p95_az0_98FtM", "stack300_vel_p95_az0_99", "pp_gather_init_2IL", "pp_gather_init_IL100"]
    lstEMVision_SynNeg_firstZ = ["stack300_vel_p95_az0_99-0_m1800"]
    lstEMVision_SynNonIntSampling = ["vpfile_BPsc1_gocad"]
    lstEMVision_HW_Data = ["EMVision_AVO_Attributes", "mnew_z100_Vp", "synthetic-horizon", "vp3d", "AVO_EMVision.vds"]
    lstIL_XL_Oriented_Data = ["prestack_In-inc_Xl-inc",
                           "prestack_In-inc_Xl-dec",
                           "prestack_In-dec_Xl-inc",
                           "prestack_In-dec_Xl-dec",

                           "prestack_Xl-inc_In-inc",
                           "prestack_Xl-inc_In-dec",
                           "prestack_Xl-dec_In-inc",
                           "prestack_Xl-dec_In-dec",

                           "poststack_In-inc_Xl-inc",
                           "poststack_In-inc_Xl-dec",
                           "poststack_In-dec_Xl-inc",
                           "poststack_In-dec_Xl-dec",

                           "poststack_Xl-inc_In-inc",
                           "poststack_Xl-inc_In-dec",
                           "poststack_Xl-dec_In-inc",
                           "poststack_Xl-dec_In-dec"
                           ]
    lstHooverGathers = [const_file_D05_Y_MIGINPUT_CMPGTHRS_HMM05()]
    lstHoover_HorizonList = ["Hoover_WB", "A70RBi_FB_XOM", "A70STi", "P110SBi", "P110STi", "Hoover_WBFt", "Hoover_WBMFt"]
    lstHoover_HorizonConvertedList = ["Hoover_WB"]
    lstHoover_SeismicList = [const_file_Hoover05APSDMFullStack(), "Hoover_05_APSDM_Full_Stack","Hoover_05_APSDM_Full_Stack_survey_coordinate_full"]
    lstHoover_VerticalFunctions_Ascii_List = ["4dmig_vf_stack_vel_t_400x400m","4dmig_vf_stack_vel_t_200x200m","4dmig_vf_rms_vel_t_400x400m","4dmig_vf_rms_vel_t_200x200m"]
    lstHoover_VelocityList = [const_file_4dmig_rms_vel_t(), const_file_VINT_IN_TIME_CORRECT_xy()]
    lstHoover_ConvertedDataList = ["Hoover_gathers", "Hoover_stack","Hoover_05_APSDM_Full_Stack_LOD3", "hoover_vel_rms", "Hoover_Vrms","Hoover_gathers_Hoover_gathers_Hoover_Vrms_[Offset_to_Angle]_[AVO_Attributes]"]
    lstHoover_Well_DeviationSurveyList = ["10379_1ST1_deviated_geom", "10379_1_deviated_geom", "10380_HA1_deviated_geom", "10380_HA3ST1_deviated_geom", "10380_HA3ST2_deviated_geom", "10380_HA3_deviated_geom", "10380_HA4BP1_deviated_geom", "10380_HA4BP2_deviated_geom", "10380_HA4_deviated_geom", "10380_HA5_deviated_geom", "10380_HA6_deviated_geom", "10381_HA2BP1_deviated_geom", "10381_HA2BP2_deviated_geom", "10381_HA2_deviated_geom", "AC025_EX_1ST1_deviated_geom", "AC025_EX_1_deviated_geom", "EB948_1ST1_deviated_geom", "EB949_1_deviated_geom", "EB949_2BP1_deviated_geom", "EB949_2_deviated_geom", "EB992_1ST_deviated_geom", "EB992_1_deviated_geom", "EB994_1ST_deviated_geom", "EB994_1_deviated_geom", "10379_1_deviated_geom_UWI", "10379_1", "EB994_1_deviated_geom_UWI", "EB994_1ST_deviated_geom_UWI", "10379_1_deviated_geom_created_for_test", "10379_1_deviated_geom_created_for_test2"]
    lstHoover_WellInventoryList = ["Hoover_well_inventory", "Hoover_well_inventory_UWI"]
    lstHoover_WellCheckshotFromDavidList = ["10380_HA3ST1_TD_EDITED"]
    lstHoover_WellCheckshotFromAlexList = ["10379_1_CKS","10379_1ST1_CKS","10380_HA1_Depth-time_P-wave","10380_HA3_CKS ","10380_HA3ST1_10380_HA3ST1_edited_TD","10380_HA3ST2_CKS","10380_HA4_CKS","10380_HA4BP1_CKS","10380_HA4BP2_CKS","10380_HA5_CKS","10380_HA6_CKS","10381_HA2_CKS","10381_HA2BP1_Depth-time_P-wave_REVIEWED","10381_HA2BP2_CKS","AC025_EX_1_Check_Shot_AC025_EX_1","AC025_EX_1ST1_CKS","EB948_1ST1_CKS","EB949_1_Marshall","EB949_2_CKS","EB949_2BP1_CKS","EB992_1_CKS","EB992_1ST_CKS","EB994_1_Check_Shot_1","EB994_1ST_CKS", "AC025_EX_1_Check_Shot_AC025_EX_1_edited_by_TT"]
    lstHoover_WellLogsList = ["10380_HA3ST1_logs_EDITED-1", "10379_1ST1_logs", "10379_1_logs-Flipped", "10379_1_logs", "10380_HA1_logs", "10380_HA3ST1_logs", "10380_HA3ST1_logs_EDITED", "10380_HA3ST2_logs", "10380_HA3_logs", "10380_HA4BP1_logs", "10380_HA4BP2_logs", "10380_HA4_logs", "10380_HA5_logs", "10380_HA6_logs", "10381_HA2BP1_logs", "10381_HA2BP2_logs", "10381_HA2_logs", "AC025_EX_1ST1_logs", "AC025_EX_1ST1_logs_TTV", "AC025_EX_1_logs", "AC025_EX_1_logs_edited", "AC025_EX_1_logs_wrong_unit_4_testing", "EB948_1ST1_logs", "EB949_1_logs", "EB949_2BP1_logs", "EB949_2_logs", "EB992_1ST_logs", "EB992_1_logs", "EB994_1ST_logs", "EB994_1_logs", "10380_HA3ST1_logs_EDITED_10380_Ha3St1", "10380_HA3ST1_logs_EDITED_-10380_--Ha3St1-", "10380_HA3ST1_logs_EDITED_10380_space_Ha3St1", "10380_HA3ST1_logs_EDITED_10380ha3st1", "10380_HA3ST1_logs_EDITED_10380-Ha3St1", "10380_HA1_logs_UWI", "10380_HA1", "EB994_1_logs_UWI", "EB994_1ST_logs_UWI"]
    lstHoover_WellMarkersList = ["10379_1ST1_tops", "10379_1_tops", "10380_HA1_tops", "10380_HA3ST1_tops", "10380_HA3_tops", "10380_HA4BP2_tops", "10380_HA4_tops", "10380_HA5_tops", "10380_HA6_tops", "10381_HA2BP1_tops", "10381_HA2_tops", "AC025_EX_1ST1_tops", "AC025_EX_1_tops", "EB948_1ST1_tops", "EB949_1_tops", "EB992_1_tops", "EB994_1ST_tops", "EB994_1_tops", "10379_1ST1_tops_UWI", "10379_1ST1", "EB994_1_tops_UWI", "EB994_1ST_tops_UWI"]
    lstHoover_VerticalFunctionAsciiList = ["4dmig_vf_rms_vel_t_200x200m", "4dmig_vf_rms_vel_t_400x400m", "4dmig_vf_stack_vel_t_200x200m", "4dmig_vf_stack_vel_t_400x400m"]
    lstHoover_4_Inlines_DataList=["Prestack_4Inlines", "Stack_4Inlines", "Vel_RMS_4Inlines","Hoover_Stack_4Inlines_survey_coordinate", "Hoover_Stack_4Inlines","Vel_RMS_4Inlines", "Stack_4InlinesFtM", "Stack_4InlinesFt", "Prestack_4InlinesFtM"]

    # "WellControl_wellHead", "WellControl_CS", "WellControl_CS_depth", "WellFast_CS", "WellFast_CS_depth", "WellSlow_CS", "WellSlow_CS_depth" removed
    #PBSyntheticFlat_List = ["MarkerMistie_wellHead", "marker_1", "marker_1_CS", "marker_2", "marker_2_CS", "marker_3", "marker_3_CS", "marker_4", "marker_4_CS", "marker_5", "marker_5_CS", "PB_synth_allVels_flat_I5C5_k55", "PB_synth_flat_depth_375.txt", "PB_synth_flat_refHor_1250", "PB_synth_flat_refHor_2000", "PB_synth_flat_refHor_2750", "PB_synth_flat_refHor_3500", "PB_synth_flat_refHor_4250", "PB_synth_flat_refHor_500", "PB_synth_flat_refHor_5000", "PB_synth_RMS_flat_I5C5_k55", "PB_synth_RMS_flat_I5C5_k55_depth", "PB_synth_RMS_w_busts_I5C5", "ScaleFactor_fast", "ScaleFactor_slow", "Vint_synthetic_depth","ModelCalibrationCalculator_flat", "WellControl_wellHead", "WellControl_CS", "WellControl_CS_depth", "WellFast_CS", "WellFast_CS_depth", "WellSlow_CS", "WellSlow_CS_depth"]
    lsthwTestingSynthetic_Well_List =  ["Deviated_well_CS", "Deviated_well_path", "Deviated_well_mrk_MD", "Deviated_well_mrk_TVDSS",
                                     "MM_well_1", "MM_well_2", "MM_well_3", "MM_well_4", "MM_well_5",
                                    "MM_well_1_CS", "MM_well_1_mrk",
                                    "MM_well_2_CS", "MM_well_2_mrk",
                                    "MM_well_3_CS", "MM_well_3_mrk",
                                    "MM_well_4_CS", "MM_well_4_mrk",
                                    "MM_well_5_CS", "MM_well_5_mrk",
                                    "MM_wellHead", "Outside_survey_CS",
                                    "S2pc_A600_CS", "S2pc_A600_path",
                                    "S2pc_B800_CS", "S2pc_B800_path",
                                    "S2pc_C1000_CS", "S2pc_C1000_path",
                                    "ScaleFactor_fast", "ScaleFactor_slow",
                                    "SeisVF_A600_CS", "SeisVF_A600_path",
                                    "SeisVF_B800_CS", "SeisVF_B800_path",
                                    "SeisVF_C1000_CS", "SeisVF_C1000_path",
                                    "SLayer_A600_CS", "SLayer_A600_CS_extreme",
                                    "SLayer_A600_path", "SLayer_B800_CS",
                                    "SLayer_B800_path", "SLayer_C1000_CS",
                                    "SLayer_C1000_path", "WellControl_CS",
                                    "WellControl_CS_depth", "WellControl_wellHead",
                                    "WellControl_CS_time","WellFast_CS_time",
                                    "WellFast_CS", "WellFast_CS_depth",
                                    "wellhead_Outside_survey", "WellHeads",
                                    "ScaleFactor_fast_depth","ScaleFactor_slow_depth",
                                     "NewWellFast_CS_time_Alex","NewWellSlow_CS_time_Alex",
                                    "WellSlow_CS", "WellSlow_CS_depth","WellSlow_CS_time",
                                    "Seam-01.GR-DT", "Seam-01.GR-DT-custom-null-value-v1",
                                    "Seam-01.GR-DT-custom-null-value-v2", "Seam-01"]
    lsthwTestingSynthetic_Interpretation_List = ["HW_dip_hor_time_200",
                                              "HW_dip_hor_time_250",
                                              "HW_dip_hor_time_500",
                                             "HW_dip_hor_time_1250",
                                             "HW_dip_hor_time_2000",
                                             "HW_dip_hor_time_2750",
                                             "HW_dip_hor_time_3500",
                                             "HW_dip_hor_time_4250",
                                             "HW_dip_hor_time_5000",
                                             "HW_flat_hor_time_200",
                                             "HW_flat_hor_time_500",
                                             "HW_flat_hor_time_1250",
                                             "HW_flat_hor_time_2000",
                                             "HW_flat_hor_time_2750",
                                             "HW_flat_hor_time_3500",
                                             "HW_flat_hor_time_4250",
                                             "HW_flat_hor_time_5000",
                                             "HW_synth_flat_depth_200",
                                             "HW_synth_flat_depth_375",
                                             "HW_synth_flat_depth_1575",
                                             "HW_synth_flat_depth_2775",
                                             "HW_synth_flat_depth_3975",
                                             "HW_synth_flat_depth_5175",
                                             "HW_synth_flat_depth_6375",
                                             "HW_synth_flat_depth_7575",
                                             "HW_flat_hor_Vint1510",
                                             "HW_synth_VintGrid"
                                             ]
    lsthwTestingSynthetic_Synthetic_Vels_4Inlines_List = ["SynthDepth_0-7380_4Inlines", "SynthDepth_0-7380_4Inlines", "SynthVel_1500-2976_4Inlines", "SynthVel_1500-2976_4Inlines"]
    lsthwTestingSynthetic_Velocities_List = ["HW_synth_allVels_flat_I5C5_k55", "HW_synth_RMS_flat_I5C5_k55", "HW_synth_RMS_flat_I5C5_k55_depth", "HW_synth_RMS_w_busts_I5C5"]
    lsthwTestingSynthetic_Data_List = ["HW_synthetic_IntVel_depth"]
    lstPBSynthRMSW_busts_I5C5_List = ["Outside_survey_CS","PB_synth_refHor_1250","PB_synth_refHor_2000","PB_synth_refHor_2750","PB_synth_refHor_3500","PB_synth_refHor_4250","PB_synth_refHor_500","PB_synth_refHor_5000","PB_synth_RMS_w_busts_I5C5","S2pc_A600_CS","S2pc_A600_path","S2pc_B800_CS","S2pc_B800_path","S2pc_C1000_CS","S2pc_C1000_path","SeisVF_A600_CS","SeisVF_A600_path","SeisVF_B800_CS","SeisVF_B800_path","SeisVF_C1000_CS","SeisVF_C1000_path","SLayer_A600_CS","SLayer_A600_CS_extreme","SLayer_A600_path","SLayer_B800_CS","SLayer_B800_path","SLayer_C1000_CS","SLayer_C1000_path","wellhead_Outside_survey","WellHeads"]
    lstPICEANCE2D_SeismicList = ["A_raw_migr_stack_FF04_01",
                              "A_raw_migr_stack_FF04_02",
                              "A_raw_migr_stack_FF04_03",
                              "A_raw_migr_stack_FF04_04",
                              "A_raw_migr_stack_LRG1",
                              "A_raw_migr_stack_LRG16",
                              "A_raw_migr_stack_LRG18",
                              "A_raw_migr_stack_LRG20",
                              "A_raw_migr_stack_LRG22",
                              "A_raw_migr_stack_LRG3",
                              "A_raw_migr_stack_LRG5"
                              ]
    lstPICEANCE2D_converted_data = ["Piceance_3D_depthVol"]
    lstPICEANCE2D_0_30_degree_angle_stack_data = ["A_angle_0-30degree_stack_FF04_01", "A_angle_0-30degree_stack_FF04_02","A_angle_0-30degree_stack_FF04_03", "A_angle_0-30degree_stack_FF04_04","A_angle_0-30degree_stack_LRG1","A_angle_0-30degree_stack_LRG3","A_angle_0-30degree_stack_LRG5","A_angle_0-30degree_stack_LRG16","A_angle_0-30degree_stack_LRG18","A_angle_0-30degree_stack_LRG20","A_angle_0-30degree_stack_LRG22"]
    lstPICEANCE2D_PostMig_CDP_NMO_data = ["PostMigration_CDP_NMO_FF04_01_031314",
                                       "PostMigration_CDP_NMO_FF04_02_031314",
                                       "PostMigration_CDP_NMO_FF04_03_031314",
                                       "PostMigration_CDP_NMO_FF04_04_031314",
                                       "PostMigration_CDP_NMO_LRG1_031314",
                                       "PostMigration_CDP_NMO_LRG16_031314",
                                       "PostMigration_CDP_NMO_LRG18_031314",
                                       "PostMigration_CDP_NMO_LRG20_031314",
                                       "PostMigration_CDP_NMO_LRG22_031314",
                                       "PostMigration_CDP_NMO_LRG3_031314",
                                       "PostMigration_CDP_NMO_LRG5_031314"
                                       ]
    lstPICEANCE2D_PreMig_CDP_noNMO_data = ["PreMigration_CDP_noNMO_FF04_01_031314",
                                       "PreMigration_CDP_noNMO_FF04_02_031314",
                                       "PreMigration_CDP_noNMO_FF04_03_031314",
                                       "PreMigration_CDP_noNMO_FF04_04_031314",
                                       "PreMigration_CDP_noNMO_LRG1_031314",
                                       "PreMigration_CDP_noNMO_LRG16_031314",
                                       "PreMigration_CDP_noNMO_LRG18_031314",
                                       "PreMigration_CDP_noNMO_LRG20_031314",
                                       "PreMigration_CDP_noNMO_LRG22_031314",
                                       "PreMigration_CDP_noNMO_LRG3_031314",
                                       "PreMigration_CDP_noNMO_LRG5_031314"
                                       ]
    lstPICEANCE2D_PostMigList = ["PostMigration_CDP_NMO_FF04_03_031314"]
    lstHoover_HorizonAttributeList = ["4dmig_vf_rms_vel_t_200x200m_Hoover_WB_CSM1500ms[HorizonAttribute]"]
    lstTera_HorizonAttributeList = ["Horizon_03_sm_attributes", "Horizon_04_sm_attributes", "Horizon_05_sm_attributes", "Horizon_06_sm_attributes", "Horizon_08_sm_attributes"]
    lstWintershall_HorizonList = ["STB02132_18_Horizon_1", "STB02132_18_Horizon_2", "STB02132_18_Horizon_3", "Horizon_01", "Horizon_02", "Horizon_03", "Horizon_04", "Horizon_05", "Horizon_06", "Horizon_01_Ft", "Horizon_01_MFt"]
    lstWintershall_ConvertedDataList = ["STB02132_14-19_prestack", "STB02132_14-19_stk","STB02132_14-19_stk_LOD3", "Finvel", "STB02132_14-19_prestack_STB02132_14-19_prestack_Vrms_[Offset_to_Angle]_[AVO_Attributes]"]

    lstWintershall_SegyFileList = ["prestack_4Inlines", "stack_4Inlines","Wintershall_stack_4Inlines_survey_coordinate","Wintershall_stack_4Inlines_survey_coordinate", "STB02132_14-19_finvel", "STB02132_14-19_prestack", "STB02132_14-19_prestack_XlincIninc", "STB02132_14-19_stk","STB02132_14-19_stk_survey_coordinate", "velocity_4Inlines",
                                "prestack_4InlinesFtM", "Wintershall_stack_4Inlines", "Wintershall_stack_4InlinesFt", "Wintershall_stack_4InlinesFtM"]

    lstWintershall_Converted_Horizon_DataList = ["Horizon_01", "Horizon_02", "Horizon_03","Horizon_04", "Horizon_05","Horizon_06"]
    lstWintershall_VerticalFunctions_Ascii_List = ["FINVEL"]
    lstWintershall_Wells_Ascii_List = ["P06B1.deviation","P06B1.markers", "P06B1.checkshot", "P06-B1_logs", "P06-B1_logs_edited", "P06B2.deviation","P06B2.markers", "P06B2.checkshot", "P06-B2_logs"]
#     lstWintershall_SegyFileList = ["STB02132_14-19_prestack", "prestack_4Inlines", "stack_4Inlines", "STB02132_14-19_finvel", "STB02132_14-19_stk", "velocity_4Inlines"]
    lsthwTestingSynthetic_Verification_spreadsheet = ["ModelCalibrationCalculator_flat"]
    lstTera_ConvertedDataList = ["Tera_prestack","Tera_AZ_small","Tera_poststack_LOD3", "Tera_RMO_IntVel", "Tera_stack", "Tera_RMO_RmsVel","Tera_prestack_Tera_prestack_Tera_RMO_IntVel_[Offset_to_Angle]_[AVO_Attributes]"]
    lstTera_list = ["13j0_rmo_gth_segy_pt01",
                "13j0_rmo_gth_segy_pt02",
                "13j0_rmo_gth_segy_pt03",
                "13j0_rmo_gth_segy_pt04",
                "13j0_rmo_gth_segy_pt05",
                "13j0_rmo_gth_segy_pt06",
                "13j0_rmo_gth_segy_pt07",
                "13j0_rmo_gth_segy_pt08",
                "13j0_rmo_gth_segy_pt09",
                "13j0_rmo_gth_segy_pt10",
                "13j0_rmo_gth_segy_pt11",
                "13j0_rmo_gth_segy_pt12",
                "13j0_rmo_gth_segy_pt13",
                "13j0_rmo_gth_segy_pt14",
                "13j0_rmo_gth_segy_pt15",
                "13j0_rmo_gth_segy_pt16",
                "13j0_rmo_gth_segy_pt17",
                "13j0_rmo_gth_segy_pt18",
                "13j0_rmo_gth_segy_pt19",
                "13j0_rmo_gth_segy_pt20",
                "13j0_rmo_gth_segy_pt21",
                "13j0_rmo_gth_segy_pt22",
                "13j0_rmo_gth_segy_pt23",
                "13j0_rmo_gth_segy_pt24",
                "13j0_rmo_gth_segy_pt25",
                "13j0_rmo_gth_segy_pt26",
                "13j0_rmo_gth_segy_pt27",
                "Tera_intVel_I17889",
                "Tera_poststack",
                "Tera_poststack_survey_coordinate",
                "Tera_prestack_I17889",
                "Tera_RMO_IntVel_export",
                "Tera_stack_I17889",
                "Tera_stack_I17889_survey_coordinate",
                "Tera_stack_I17889Ft",
                "Tera_stack_I17889FtM",
                "Tera_prestack_I17889FtM"]
    lstTera_wellHead_list = ["Tera_well_inventory_AK"]
    lstTera_wellCS_list = ["22_01-1A_Cheap",
                        "22_01-2B_Cheap",
                        "22_01-2B_Direct",
                        "22_02-1_Cheap",
                        "22_04-1_Cheap",
                        "22_09-1_Cheap",
                        "22_10a-1_Cheap",
                        "22_11-1_Cheap"
                        ]
    lstTera_wellCS_ZZZ_list = ["22_04-1_CKS",
                            "22_11-1_CKS",
                            "22_01-1A_CKS",
                            "22_02-1_CKS",
                            "22_10a-1_CKS",
                            "22_09-1_CKS",
                            "22_01-2B_CKS"
                            ]
    lstTera_wellPath_list = ["22_01-2B_deviated_geom",
                        "22_10a-1_deviated_geom",
                        "22_11-1_path",
                        "22_09-1_path",
                        "22_11-1_deviated_geom",
                        "22_01-1A_path",
                        "22_01-1A_deviated_geom",
                        "22_04-1_path",
                        "22_09-1_deviated_geom",
                        "22_01-1B_path",
                        "22_04-1_deviated_geom",
                        "22_10a-1_path",
                        "22_02-1_path",
                        "22_02-1_deviated_geom",
                          ]
    lstSyntheticWellpath = ["sEaM-07", "Seam-01", "Seam-03", "Seam-02", "Seam-05", "Seam-04", "SeAM --- --09 -- -", "Seam--08--", "Seam-06A", "junk"]
    
    lstTera_velocity_list = ["Tera_velPicks_from_semb_dec","Tera_velPicks_from_semb_noWB"]
    
    lstTera_horizon_list = ["Horizon_01_sm",
                         "Horizon_02_sm",
                         "Horizon_03_sm",
                         "Horizon_04_sm",
                         "Horizon_05_sm",
                         "Horizon_06_sm",
                         "Horizon_07_sm",
                         "Horizon_08_sm",
                         "Horizon_09_sm",
                         "WB_sm",
#                          "WB",
#                          "Horizon_01",
#                          "Horizon_02",
#                          "Horizon_03",
#                          "Horizon_04",
#                          "Horizon_05"
                         ]
    lstTera_horizons_list = ["Model_130", "WB", "Horizon_01", "Horizon_02", "Horizon_03", "Horizon_04", "Horizon_05", "Horizon_06", "Horizon_07", "Horizon_08", "Horizon_09","Tera_velPicks_from_semb_dec_WB_sm_CSM1500ms[HorizonAttribute]_new_r27130"]
    latTera_velocities_list = ["Tera_velPicks_from_semb_dec","Tera_velPicks_from_semb_noWB"]
    lstTera_converted_gather = ["Tera_prestack_AZ_034"]
    lstHWTMP_8151_WellMarkersList = ["B-41"]
    lstWAZData =   ["WAZ_11-20_az",
                    "WAZ_211-220",
                    "WAZ_01-10",
                    "WAZ_61-70",
                    "WAZ_311-320",
                    "WAZ_41-50",
                    "WAZ_51-60",
                    "WAZ_151-160",
                    "WAZ_121-130",
                    "WAZ_341-350",
                    "WAZ_01-10_az",
                    "WAZ_181-190",
                    "WAZ_261-270",
                    "WAZ_251-260",
                    "WAZ_291-300",
                    "WAZ_31-40",
                    "WAZ_91-100",
                    "WAZ_111-120",
                    "WAZ_71-80",
                    "WAZ_31-40_az",
                    "WAZ_241-250",
                    "WAZ_231-240",
                    "WAZ_81-90",
                    "WAZ_11-20",
                    "WAZ_351-360",
                    "WAZ_221-230",
                    "WAZ_101-110",
                    "WAZ_321-330",
                    "WAZ_191-200",
                    "WAZ_161-170",
                    "WAZ_141-150",
                    "WAZ_131-140",
                    "WAZ_201-210",
                    "WAZ_331-340",
                    "WAZ_171-180",
                    "WAZ_21-30",
                    "WAZ_281-290",
                    "WAZ_21-30_az",
                    "WAZ_271-280",
                    "WAZ_301-310"
                  ]
    lstTesting_WorkspaceAndData_Data = ["HW_Synthetic_2D_prestack_time", "HW_Synthetic_timeVol_depth", "HW_Synthetic_Vrms_time", "Synthetic_velocity_1mps_per_samp_depth", "HW_Synthetic_timeVol_depth", "HW_Synthetic_Vavg_time", "Synthetic_velocity_1mps_per_samp_time", "HW_Synthetic_prestack_time", "HW_Synthetic_stack_time_5_Inlines", "HW_Synthetic_2D_stack_time", "HW_Synthetic_prestack_time_5_Inlines", "HW_Synthetic_2D_prestack_depth", "HW_Synthetic_2D_stack_time", "VelocityConversion", "HW_Synthetic_depthVol_time", "HW_Synthetic_prestack_depth", "HW_Synthetic_2D_stack_depth", "HW_Synthetic_Vavg_depth", "HW_Synthetic_depthVol_time", "HW_Synthetic_Vint_depth", "HW_Synthetic_stack_time", "HW_Synthetic_stack_depth", "HW_Synthetic_Vint_time", "VelocityConversion_time", "VelocityConversion_depth"]
    lstHWSynthetic = ["HW_synth_flat_velocity_1500"]
#     lstEdvardGrieg_16_1_13 = ["WELLPATH_ORIGINAL_SURVEY_POINTS_1", "WELLPATH_ORIGINAL_SURVEY_POINTS_1-MOD", "TZV_DEPTH_MD_CHECKSHOT_1", "16_1-13", "16_1-13-TZV_DEPTH_MD_CHECKSHOT_1"]
    lstEdvardGrieg_16_1_8 = ["WELLPATH_ORIGINAL_SURVEY_POINTS_1", "16_1-8-TZV_DEPTH_MD_CHECKSHOT_1", "16_1-8", "TZV_DEPTH_MD_CHECKSHOT_1"]
    lstEdvardGrieg_16_1_13 = ["WELLPATH_ORIGINAL_SURVEY_POINTS_1-MOD", "16_1-13-TZV_DEPTH_MD_CHECKSHOT_1", "16_1-8", "TZV_DEPTH_MD_CHECKSHOT_1"]
#     PB_systhetic_flat_ListFile = ["PB_synth_flat_refHor_500", "PB_synth_flat_refHor_1250","PB_synth_flat_refHor_2000","PB_synth_flat_refHor_2750","PB_synth_flat_refHor_3500", "PB_synth_flat_refHor_4250", "PB_synth_flat_refHor_5000",
#                                   "MarkerMistie_wellHead",
#                                   "marker_1_CS", "marker_2_CS", "marker_3_CS", "marker_4_CS", "marker_5_CS",
#                                   "marker_1", "marker_2", "marker_3", "marker_4", "marker_5"]
    # Added by sms.neo.trinh
#     wellLogFileList = ["MM_well_1", "MM_well_2", "MM_well_3", "MM_well_4", "MM_well_5"]

    lstWG = ["blackstone_headwave_immo_vol_SEGY_2", "gathers_corrected", "pegasus_vol_pgrid_to_input_Headwave", "pegasus_vol_pgrid_to_input_Headwave_withHeader"]
    lstOverlapIL = ["8282_last2_IL", "8482_first2_IL"]
    lstGeoprocesados = ["xl64ES360_REFL_GATHERS_ap12Kdesp_precon", "cdp-gathers", "ffid_026-046", "ES360_REFL_GATHERS_ap12Kdesp_precon", "shots_with_geometry"]
    lstSeamTS = ["seam_multi_z_t_surf.ts", "seammultiztsurfnegatedvalues_1602085906"]
    
    lstNovaScotia = ["Nova_Scotia_pstm_stack"]
    lstNovaScotiaGathers = ["3D_gathers_pstm_nmo_X1521-1560", "3D_gathers_pstm_nmo_X1561-1600"]
    
    lstPolarcusTrim = ["MC1501-1252P1090_Trim_1_27500"]
    
    if strExtension == "vds":
#         if com_listContains(lstLundinList, strFileName):
        if com_listContains(lstLundinList_Converted_SMS, strFileName):
            strPath = "%s/HW_Data/Edvard_Grieg/SMS/%s.vds" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstLundinConvertedFiles_List, strFileName):
            strPath = "%s/HW_Data/Edvard_Grieg/%s.vds" % (com_getHWDataPath(), strFileName)    
        elif com_listContains(lstWAZList, strFileName):
            strPath = "%s/Data/Testing/Workspaces_and_Data/Data/WAZ/%s.vds" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstWintershall_ConvertedDataList, strFileName):
            strPath = "%s/HW_Data/Wintershall/%s.vds" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstTera_ConvertedDataList, strFileName):
            strPath = "%s/HW_Data/Tera/%s.vds" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstHoover_ConvertedDataList, strFileName):
            strPath = "%s/HW_Data/Hoover/%s.vds" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstTera_converted_gather, strFileName):
            strPath = "%s/HW_Data/Tera/Wide_Azimuth/%s.vds" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstWG, strFileName):
            strPath = "%s/Data/WG/%s.vds" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstEMVision_HW_Data, strFileName):
            strPath = "%s/HW_Data/EMVision/%s.vds" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstWintershall_HorizonList, strFileName) and strDataset != "Tera":
            strPath = "%s/Interpretation/Wintershall/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)

    elif strExtension == "":
        if com_listContains(lstLundinConvertedFiles_List, strFileName):
            strPath = "%s/HW_Data/Edvard_Grieg/%s" % (com_getHWDataPath(), strFileName)    
        elif com_listContains(lstPICEANCE2D_SeismicList, strFileName):
            strPath = "%s/Data/PICEANCE-2D/Seismic/Raw migration stack/%s" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstHoover_ConvertedDataList, strFileName):
            strPath = "%s/HW_Data/Hoover/%s" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lsthwTestingSynthetic_Well_List, strFileName):
            strPath = "%s/Data/Testing/Workspaces_and_Data/Wells/%s" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lsthwTestingSynthetic_Interpretation_List, strFileName):
            strPath = "%s/Data/Testing/Workspaces_and_Data/Interpretation/%s" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lsthwTestingSynthetic_Synthetic_Vels_4Inlines_List, strFileName):
            strPath = "%s/Data/Testing/Synthetic/Synthetic_Vels_4Inlines/%s" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lsthwTestingSynthetic_Velocities_List, strFileName):
            strPath = "%s/Data/Testing/Workspaces_and_Data/Velocities/%s" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lsthwTestingSynthetic_Data_List, strFileName):
            strPath = "%s/Data/_archive/Testing/Synthetic/Data/%s" % (com_getHWDataPath(), strFileName)
#         elif com_listContains(PBSyntheticFlat_List, strFileName):
#             strPath = "%s/Data/Testing/Synthetic/Old_synthetic_do_not_use/PB_synthetic_flat/%s" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lsthwTestingSynthetic_Verification_spreadsheet, strFileName):
            strPath = "%s/Data/_archive/Testing/Synthetic/Old_synthetic_do_not_use/PB_synthetic_flat/%s" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstWintershall_ConvertedDataList, strFileName):
            strPath = "%s/HW_Data/Wintershall/%s" % (com_getHWDataPath(), strFileName)
        #elif com_listContains(lstWintershall_Converted_Horizon_DataList, strFileName):
        #    strPath = "%s/HW_Data/Wintershall/horizons/%s" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstPICEANCE2D_0_30_degree_angle_stack_data, strFileName):
            strPath = "%s/Data/PICEANCE-2D/Seismic/0-30 degree angle stack/%s" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstPICEANCE2D_converted_data, strFileName):
            strPath = "%s/HW_Data/PICEANCE-2D/%s" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstTera_ConvertedDataList, strFileName):
            strPath = "%s/HW_Data/Tera/%s" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstTesting_WorkspaceAndData_Data, strFileName):
            strPath = "%s/Data/Testing/Workspaces_and_Data/Data/%s" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstHWSynthetic, strFileName):
            strPath = "%s/Data/Testing/Velocities/HW_Synthetic/%s" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstWintershall_HorizonList, strFileName) and strDataset != "Tera":
            strPath = "%s/Interpretation/Wintershall/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)    
        elif com_listContains(lstTera_horizon_list, strFileName):
            strPath = "%s/Interpretation/Tera/%s" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstHoover_HorizonConvertedList, strFileName):
            strPath = "%s/Interpretation/Hoover/%s" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstWAZData, strFileName):
            strPath = "%s/Data/Testing/Workspaces_and_Data/Data/WAZ/%s" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstLundinList, strFileName) :
            strPath = "%s/Data/Lundin/%s" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstEMVision_HW_Data, strFileName):
            strPath = "%s/HW_Data/EMVision/%s" % (com_getHWDataPath(), strFileName)
        elif com_listContains(lstPolarcusTrim, strFileName):
            strPath = "%s/Data/Polarcus/Trim/%s" % (com_getHWDataPath(), strFileName)
    else:
        if com_listContains(lstColorTable, strFileName) :
            strPath = "%s/Data/Testing/Data/color_table/%s.%s" % (com_getHWDataPath(), strFileName, strExtension) 
        elif com_listContains(lstEMVisionList, strFileName) :
            strPath = "%s/Data/EMVision/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstLundinList, strFileName) :
            strPath = "%s/Data/Lundin/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstEMVision_SamplingHorizon_List, strFileName) :
            strPath = "%s/Data/EMVision/sampling_horizon_and_volume_tsurf_data/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstEMVision_405_voxet_List, strFileName) :
            strPath = "%s/Data/EMVision/emv-405-voxet-arranged-as-depth-slices/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstEMVision_Mixed_Units_Manual, strFileName) :
            strPath = "%s/Data/EMVision/mixed_units_manual_testing_script_and_associated_data/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstEMVision_SynNeg_firstZ, strFileName):
            strPath = "%s/Data/EMVision/synthetic_w_negative_first_Z/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstEMVision_SynNonIntSampling, strFileName):
            strPath = "%s/Data/EMVision/synthetic_non_integer_sampling/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstIL_XL_Oriented_Data, strFileName) :
            strPath = "%s/Data/Testing/Workspaces_and_Data/Data/Importer_Tests/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstOverlapIL, strFileName) :
            strPath = "%s/Data/Testing/Workspaces_and_Data/Data/HWTMP-8201/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstHoover_HorizonList, strFileName):
            strPath = "%s/Interpretation/Hoover/ascii/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstHoover_SeismicList, strFileName):
            strPath = "%s/Data/Hoover/seismic/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstHoover_VerticalFunctions_Ascii_List, strFileName):
            strPath = "%s/Velocities/Hoover/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstPICEANCE2D_SeismicList, strFileName):
            strPath = "%s/Data/PICEANCE-2D/Seismic/Raw migration stack/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstPICEANCE2D_PostMigList, strFileName):
            strPath = "%s/Data/PICEANCE-2D/PostMig_CDP_NMO/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstHoover_VelocityList, strFileName):
            strPath = "%s/Data/Hoover/velocity models/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstHoover_Well_DeviationSurveyList, strFileName):
            strPath = "%s/Wells/Hoover/deviation surveys/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstHoover_WellInventoryList, strFileName):
            strPath = "%s/Wells/Hoover/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstHoover_WellCheckshotFromDavidList, strFileName):
            strPath = "%s/Wells/Hoover/checkshots_from_David/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstHoover_WellCheckshotFromAlexList, strFileName):
            strPath = "%s/Wells/Hoover/checkshots_from_Alex/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstWintershall_HorizonList, strFileName) and strDataset != "Tera":
            strPath = "%s/Interpretation/Wintershall/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstWintershall_SegyFileList, strFileName):
            strPath = "%s/Data/Wintershall/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstWintershall_VerticalFunctions_Ascii_List, strFileName):
            strExtension = const_extensionFileASCII()
            strPath = "%s/Velocities/Wintershall/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)          
        elif com_listContains(lstWintershall_Wells_Ascii_List, strFileName):
            strPath = "%s/Wells/Wintershall/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)          
        elif com_listContains(lsthwTestingSynthetic_Well_List, strFileName):
            strPath = "%s/Data/Testing/Workspaces_and_Data/Wells/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lsthwTestingSynthetic_Interpretation_List, strFileName):
            strPath = "%s/Data/Testing/Workspaces_and_Data/Interpretation/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lsthwTestingSynthetic_Synthetic_Vels_4Inlines_List, strFileName):
            strPath = "%s/Data/Testing/Synthetic/Synthetic_Vels_4Inlines/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lsthwTestingSynthetic_Velocities_List, strFileName):
            strPath = "%s/Data/Testing/Workspaces_and_Data/Velocities/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lsthwTestingSynthetic_Verification_spreadsheet, strFileName):
            strPath = "%s/Data/_archive/Testing/Synthetic/Old_synthetic_do_not_use/PB_synthetic_flat/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstHoover_WellLogsList, strFileName):
            strPath = "%s/Wells/Hoover/logs/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstHoover_WellMarkersList, strFileName):
            strPath = "%s/Wells/Hoover/tops/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstHWTMP_8151_WellMarkersList, strFileName):
            strPath = "%s/Wells/HWTMP-8151/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstPBSynthRMSW_busts_I5C5_List, strFileName):
            strPath = "%s/Data/PB_synth_RMS_w_busts_I5C5/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstHoover_VerticalFunctionAsciiList, strFileName):
            strPath = "%s/Velocities/Hoover/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstHooverGathers, strFileName):
            strPath = "%s/Data/Hoover/gathers/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstPICEANCE2D_PostMig_CDP_NMO_data, strFileName):
            strPath = "%s/Data/PICEANCE-2D/PostMig_CDP_NMO/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstPICEANCE2D_PreMig_CDP_noNMO_data, strFileName):
            strPath = "%s/Data/PICEANCE-2D/PreMig_CDP_noNMO/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstTesting_WorkspaceAndData_Data, strFileName):
            strPath = "%s/Data/Testing/Workspaces_and_Data/Data/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstHoover_4_Inlines_DataList, strFileName):
            strPath = "%s/Data/Hoover/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstHWSynthetic, strFileName):
            strPath = "%s/Data/Testing/Velocities/HW_Synthetic/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
#         elif com_listContains(lstWintershall_SegyFileList, strFileName):
#             strPath = "%s/Data/Wintershall/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstTera_list, strFileName):
            strPath = "%s/Data/PGS/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstTera_wellHead_list, strFileName):
            strPath = "%s/Wells/Tera/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstTera_wellCS_list, strFileName):
            strPath = "%s/Wells/Tera/Checkshots/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstTera_wellCS_ZZZ_list, strFileName):
            strPath = "%s/Wells/Tera/Checkshots/ZZZ/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstTera_wellPath_list, strFileName):
            strPath = "%s/Wells/Tera/Paths/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
#         elif com_listContains(lstTera_velocity_list, strFileName):
#             strPath = "%s/Data/Quad22/Velocity/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstTera_horizon_list, strFileName):
            strPath = "%s/Interpretation/Tera/Smooth_model_horizons/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstSurface_models_SMF, strFileName):
            strPath = "%s/Data/Testing/Data/Surface_models/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstSurface_model_SMF_EMVision, strFileName):
            strPath = "%s/Data/EMVision/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstWintershall_HorizonList, strFileName) and strDataset != "Tera":
            strPath = "%s/Interpretation/Wintershall/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstTera_horizons_list, strFileName) and strDataset != "Wintershall":
            strPath = "%s/Interpretation/Tera/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(latTera_velocities_list, strFileName):
            strPath = "%s/Velocities/Tera/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstHoover_HorizonAttributeList, strFileName):
            strPath = "%s/Interpretation/Hoover/ascii/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstTera_HorizonAttributeList, strFileName):
            strPath = "%s/Interpretation/Tera/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstWAZData, strFileName):
            strPath = "%s/Data/Testing/Workspaces_and_Data/Data/WAZ/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstEdvardGrieg_16_1_8, strFileName):
            strPath = "%s/Wells/Edvard_Grieg/16_1-8/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstEdvardGrieg_16_1_13, strFileName):
            strPath = "%s/Wells/Edvard_Grieg/16_1-13/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstSyntheticWellpath, strFileName):
            strPath = "%s/Data/Testing/Wells/Testing/Well_Marker/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstWG, strFileName):
            strPath = "%s/Data/WG/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstGeoprocesados, strFileName):
            strPath = "%s/Data/Geoprocesados/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstSeamTS, strFileName):
            strPath = "%s/Data/Testing/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstNovaScotia, strFileName):
            strPath = "%s/Data/Nova_Scotia/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        elif com_listContains(lstNovaScotiaGathers, strFileName):
            strPath = "%s/Data/Nova_Scotia/Gathers/%s.%s" % (com_getHWDataPath(), strFileName, strExtension)
        
    return strPath
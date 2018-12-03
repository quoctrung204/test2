################# Data types #################
def const_dataTypePrestack():
    return "Prestack"

def const_dataTypePoststack():
    return "Poststack"

def const_dataType2DPrestack():
    return "2DPrestack"

def const_dataType2DPoststack():
    return "2DPoststack"

def const_dataTypeHorizon():
    return "Horizon"

############ >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Project tree constant object name  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def const_avoInterceptName():
    return "Intercept.DisplayName"
# [PoststackObject.Intercept.DisplayName.CustomLineEditWidget]

def const_avoGradientName():
    return "Gradient.DisplayName"
# [PoststackObject.Intercept.DisplayName.CustomLineEditWidget]

def const_velocityPickEditorWorkflow():
    return "[Workflow.DisplayName.CustomLineEditWidget]"

def const_velocityModelName():
    return "VelocityModel"
    
def const_wellContainerName():
    return "[WellContainer.DisplayName.CustomLineEditWidget]"

def const_verticalFunctionName():
    return "[FreeFormVerticalFunctionSetVelocity.DisplayName.CustomLineEditWidget]"

def const_3DSurvey():
    return ".Survey3DObject."
    
def const_pickedTriangleSurface():
    return ".PickedTriangleSet."

def const_horizonFromShape():
    return ".HorizonFromShape."

def const_freeformPointset():
    return ".FreeFormPointSet."

# def const_velocityMistieControlPointName():
#     return "ShapeLinePointSet.DisplayName.CustomLineEditWidget"

def const_velocityControlPointName():
    return "Velocity control points"

def const_mistieControlPointName():
    return "Mistie control points"

def const_wellMistieMontrolGroupName():
    return "Group"

def const_wellMarkersContainer():
    return "WellMarkerContainer"

def const_SEGYExporterPlugin():
    return "SEGYExporterPlugin"

def const_GoCadExporterPlugin():
    return "GoCadExporter"

def const_ZGYExporterPlugin():
    return "ZGYExporter"

def const_HorizonExporterPlugin():
    return "HWHorizonExporter"

def const_PetrelExporterPlugin():
    return "HWPetrelExportObject"

# To .ascii vertical function file'
def const_HWVerticalFunctionExporterPlugin():
    return "HWVerticalFunctionExporters"

# Vertical function sets
def const_VerticaFunctionset():
    return "VerticalFunctionSetContainer"

def const_PetrelDataHubContainer():
#     return "[LogicalObjectTreeCanvas0.DataHub.DisplayName.CustomLineEditWidget]"
    return "{Object:DataHub:DisplayName}.ObjectPlaceholderWidget"

def const_PetrelInstanceResource():
    return "PetrelInstanceResource."

def const_menuViews():
    return "View"

def const_menuWorkflow():
    return "Workflows"

def const_menuSpectralDecompositionWorkflow():
    return "Spectral Decomposition"

def const_menuCLSSARGBBlendingWorkflow():
    return "8716604800061089128"

def const_menuGroupAVO():
    if conf_isTrunk():
        return "Avo"
    else:
        return "AVO"
    
def const_menuGroupSQIAVO():
    return "SQI AVO"

def const_menuGroupInterpretation():
    return "Interpretation"

def const_workflowFindAVOFeature():
    return "6258615794579347842"

def const_workflowAVOCrossplot():
#     return "9165792472433060706"
#     return "3426030631028695403"
#     return "4994435699450682800"
#     return "8929939152904990759"
    return "AVO Crossplot"

def const_workflowPickHorizons():
    return "1705662061906531792"

def const_VelocityPickEditor():
    return "6333502826826091574"

def const_InVA_Corrected():
    return "Velocity Analysis - Corrected Gathers Input"

def const_InVA_Uncorrected():
    return "Velocity Analysis - Uncorrected Gathers Input"

def const_AzimuthOffsetWorkflow():
    return "Azimuth/Offset"

def const_menuVelocityModelBoundaryGroup():
    return "Velocity model boundary group"
#     return "6844489037219905190"#.Groups.{Misc:Groups}Item"

def const_menuWellMistieControlGroup():
    return "Well*istie*ontrol*roup"
#     return "6844489037219905513.Groups.{Misc:Groups}Item"

def const_attDepthMistie():
    return "Depth*istie"
    
def const_ImportPetrelPoststack():
    return "ImportPetrelPoststackResource"

def const_ImportPetrelHorizon():
    return "ImportPetrelHorizonResource"

def const_ImportPetrelHorizonAttribute():
    return "ImportPetrelHorizonAttributeResource"

def const_ImportPetrel2DSeismic():
    return "ImportPetrelStacked2DLineResource"
# "Absolute location data link"
def const_AbsoluteLocationDataLink():
#     return "Absolute location data link"
    return "CreateAbsoluteLocationDataLink"

def const_RelativeLocationDataLink():
    return "CreateRelativeLocationDataLink"
#     return "Relative location"

def const_RemoveDataLink():
    return "Data link"
# Copy Horizon Bin Grid
def const_CopyHorizonBinGrid():
    return "CopyHorizonLattice"

def const_ImportPetrelWellHead():
    return "ImportPetrelWellResources"

def const_ImportPetrelClosestMatchingWell():
    return "ImportPetrelClosestMatchingWellResources"

def const_ImportPetrelNoMatchingWell():
    return "ImportPetrelNoMatchingWellResources"

def const_ImportPetrelUWIMatchingWell():
    return "ImportPetrelUWIMatchingWellResources"

def const_ImportPetrelWellPath():
    return "ImportPetrelWellPathResources"

def const_ImportOriginalPetrelClosestMatchingWellPath():
    return "ImportPetrelWellPathClosestNameMatchingResources"

def const_ImportOriginalPetrelNoMatchingWellPath():
    return "ImportPetrelWellPathNoNameMatchingResources"

def const_ImportOriginalPetrelUWIMatchingWellPath():
    return "ImportOriginalPetrelWellPathUWIMatchingResources"

def const_ImportPetrelWellCalculatedPath():
    return "ImportCalculatedPetrelWellPathResources"

def const_ImportPetrelClosestMatchingWellCalculatedPath():
    return "ImportCalculatedPetrelWellPathClosestNameMatchingResources"

def const_ImportPetrelNoMatchingWellCalculatedPath():
    return "ImportCalculatedPetrelWellPathNoNameMatchingResources"

def const_ImportPetrelUWIMatchingWellCalculatedPath():
    return "ImportCalculatedPetrelWellPathUWIMatchingResources"

def const_ImportPetrelWellLog():
    return "ImportPetrelWellLogResources"

def const_ImportPetrelWellCheckShot():
    return "ImportPetrelWellCheckshotResources"

def const_ImportPetrelClosestWellLog():
    return "ImportPetrelWellLogClosestMatchingResources"

def const_ImportPetrelNoMatchingWellLog():
    return "ImportPetrelWellLogNoMatchingResources"

def const_ImportPetrelUWIMatchingWellLog():
    return "ImportPetrelWellLogUWIMatchingResources"

def const_ImportClosestMatchingPetrelWellCheckShot():
    return "ImportPetrelWellCheckshotClosestNameResources"

def const_ImportNoMatchingPetrelWellCheckShot():
    return "ImportPetrelWellCheckshotNoNameResources"

def const_ImportUWIMatchingPetrelWellCheckShot():
    return "ImportPetrelWellCheckshotUWIMatchingResources"



def const_ImportPetrelWellMarker():
    return "ImportPetrelWellMarkerResources"

def const_ImportPetrelClosestWellMarker():
    return "ImportPetrelWellMarkerClosestMatchingNameResources"

def const_ImportPetrelNoMatchingWellMarker():
    return "ImportPetrelWellMarkerNoMatchingNameResources"

def const_ImportPetrelUWIMatchingWellMarker():
    return "ImportPetrelWellMarkerUWIMatchingNameResources"

def const_ImportAllPetrelWellComponets():
    return "ImportAllPetrelWellComponentsResources"

def const_ImportPetrelTriangleSurface():
    return "ImportPetrelTriangulatedSurfaceResources"

def const_ImportPetrelFault():
    return "ImportPetrelPolylineSetResource"

def const_ImportPetrelCulturalData():
    return "ImportPetrelPolygonSetResource"

def const_ImportPetrelPointSet():
    return "ImportPetrelPointSetResource"

def const_EventNewOnChangeOfPetrel():
    return "SubscribeCreateNewOnChangeOfPetrel"

def const_EventNotifyOnChangeOfPetrel():
    return "SubscribeNotifyOnChangeOfPetrel"

def const_EventOverwriteOnChangeOfPetrel():
    return "SubscribeOverwriteOnChangeOfPetrel"

def const_NoEventOnChangeOfPetrel():
    return "UnsubscribeOnChangeOfPetrel"

def const_AddPetrelInstance():
    return "ImportPetrelLinkPlugin"

############################################# Pointset algorithms ###############################################

## Line set
def const_lineSetContextMenu():
    return "Line set" 

def const_IntersectionLineSetContextMenu():
    if conf_isStaging():
        return "Intersection Line Set"
    else:
        return "Intersection line set"

def const_deriveLineset():
    return [const_algExtrudedLineSet(),
        const_algBorderLineSet(),
        const_algMergedLineSet()]

# Extruded Line Set': [createExtrudedLineSet.1.Extruded Line Set.Invoke]'
def const_algExtrudedLineSet():
    return "createExtrudedLineSet"

def const_algMergedLineSet():
    return "Merged line set"


## Point set
def const_pointsetContextMenu():
    return "Point set"

def const_derivePointset():
    return [const_algSimplifiedPointSet(),
        const_algSubsetPointSet(),
        const_algValuespaceMappedPointset(),
        const_algMergedPointSet()]

# Simplified Point Set': [createSimplifiedPointSet.1.Simplified Point Set.Invoke]'
def const_algSimplifiedPointSet():
    return "createSimplifiedPointSet"

# Subset Point Set': [createSubsetPointSet.1.Subset Point Set.Invoke]'
def const_algSubsetPointSet():
    return "createSubsetPointSet"
    
# Value space mapped Point Set': [createMappedPointSet.1.Value space mapped Point Set.Invoke]'
def const_algValuespaceMappedPointset():
    return "createMappedPointSet"

def const_algMergedPointSet():
    return "Merged point set"

## Polygon Set': [Polygon Set.ChildMenu.Polygon SetItem.1396441202]'
def const_polygonSetContextMenu():
    return "Polygon Set"

def const_derivePolygonSet():
    return [const_algConvexHullPolygonSurface(),
        const_algCleanedPolygonSurface(),
        const_algPatchedPolygonSurface(),
        const_algSimplifiedPolygonSurface(),
        const_algValuespaceMappedPolygonSurface(),
        const_algMergedPolygonSet()]
    
# Convex Hull polygon surface': [createConvexHullPolygonSet.1.Convex Hull polygon surface.Invoke]'
def const_algConvexHullPolygonSurface():
    return "createConvexHullPolygonSet"

def const_algMergedPolygonSet():
    return "Merged polygon set"

## Polyline Set': [Polyline Set.ChildMenu.Polyline SetItem.1396441202]'
def const_polylineSetContextMenu():
    return "Polyline Set"

def const_derivePolylineSet():
    return [const_algExtrudedPolylineSet(),
        const_algPickedPolylineSet(),
        const_algBorderPolylineSet(),
        const_algMergedPolylineSet()]

# Extruded Polyline Set': [createExtrudedPolylineSet.1.Extruded Polyline Set.Invoke]'
def const_algExtrudedPolylineSet():
    return "createExtrudedPolylineSet"

def const_algMergedPolylineSet():
    return "Merged polyline set"

# Picked polyline set': [createPickedPolylineSet.1.Picked polyline set.Invoke]'
def const_algPickedPolylineSet():
    return "createPickedPolylineSet"

## Scalar Primitive Property': [Scalar Primitive Property.ChildMenu.Scalar Primitive PropertyItem.1396441202]'
def const_scalarPrimitiveProperty():
    #return "Scalar Primitive Property"
    return "Scalar point property"

def const_scalarPointProperty():
    #return "Scalar Primitive Property"
    return "Scalar point property"

def const_scalarTriangleProperty():
    #return "Scalar Primitive Property"
    return "Scalar triangle property"

def const_deriveScalarPointProperty():
    return [const_algScalarPointInfoProperty(),
        ]

def const_deriveScalarTriangleProperty():
    return [const_algScalarTriangleInfoProperty(),
        ]
        
def const_deriveScalarPrimitiveProperty():
    return [const_algScalarPointInfoProperty(),
        const_algScalarTriangleInfoProperty()]
    
# Scalar point info property': [createScalarPointInfoProperty.1.Scalar point info property.Invoke]'
def const_algScalarPointInfoProperty():
    #return "createScalarPointInfoProperty"
    return "Scalar point info property"

## Scalar Vertex Property': [Scalar Vertex Property.ChildMenu.Scalar Vertex PropertyItem.1396441202]'
def const_scalarVertexPropertyContextMenu():
    return "Scalar vertex property"

def const_deriveScalarVertexProperty():
    return [const_algScalarVertexInfoProperty()]
# Scalar vertex info property': [createScalarVertexInfoProperty.1.Scalar vertex info property.Invoke]'
def const_algScalarVertexInfoProperty():
    #return "createScalarVertexInfoProperty"
    return "Scalar vertex info property"

## Three-Component Primitive Property': [Three-Component Primitive Property.ChildMenu.Three-Component Primitive PropertyItem.1396441202]'
def const_threeComponentPrimitivePropertyContextMenu():
    #return "Vector3 primitive property"
    return "Three-component point property" 
def const_threeComponentPointPropertyContextMenu():
    #return "Vector3 primitive property"
    return "Three-component point property"
def const_threeComponentTrianglePropertyContextMenu():
    #return "Vector3 primitive property"
    return "Three-component triangle property"

def const_deriveThreeComponentPrimitiveProperty():
    return [const_algVector3PointInfoProperty(),
        const_algVector3TriangleInfoProperty()]

def const_deriveThreeComponentPointProperty():
    return [const_algVector3PointInfoProperty(),
        ]

def const_deriveThreeComponentTriangleProperty():
    return [const_algVector3TriangleInfoProperty()]
        
# Vector3 point info property': [createVector3PointInfoProperty.1.Vector3 point info property.Invoke]'
def const_algVector3PointInfoProperty():
    #return "createVector3PointInfoProperty"
    return "Three-component point info property" 

## Three-Component Vertex Property': [Three-Component Vertex Property.ChildMenu.Three-Component Vertex PropertyItem.1396441202]'
def const_threeComponentVertexPropertyContextMenu():
    #return "Vector3 Vertex Property"
    return "Three-component vertex property"
def const_deriveThreeComponentVertexProperty():
    return [const_algVector3VertexInfoProperty()]

# Vector3 vertex info property': [createVector3VertexInfoProperty.1.Vector3 vertex info property.Invoke]'
def const_algVector3VertexInfoProperty():
#     return "createVector3VertexInfoProperty"
    return "Three-component vertex info property"

## Triangle Set': [Triangle Set.ChildMenu.Triangle SetItem.1396441202]'
def const_triangleSetContextMenu():
    return "Triangle surface"

def const_deriveTriangleSet():
    return [const_algConvexHullTriangleSurface(),
        const_algPickedTriangleSurface(),
        const_algVerticalArbitrarySection(),
        const_algCleanedTriangleSurface(),
        const_algPatchedTriangleSurface(),
        const_algSimplifiedTriangleSurface(),
        const_algSubsetTriangleSurface(),
        const_algValueSpaceMappedTriangleSurface(),
        const_algSubdividedTriangleSet(),
        const_algMergedTriangleSet()]

def const_algMergedTriangleSet():
    return "Merged triangle set"

# Convex Hull triangle surface': [createConvexHullTriangleSet.1.Convex Hull triangle surface.Invoke]'
def const_algConvexHullTriangleSurface():
    return "createConvexHullTriangleSet"

# Picked triangle surface': [createPickedTriangleSet.1.Picked triangle surface.Invoke]'
def const_algPickedTriangleSurface():
    return "createPickedTriangleSet"

# Vertical arbitrary section': [createVerticalArbitrarySection.1.Vertical arbitrary section.Invoke]'
def const_algVerticalArbitrarySection():
    return "createVerticalArbitrarySection"

############################################# Triangle surface algorithms ###############################################

## Line Set': [Line Set.ChildMenu.Line SetItem.1396441202]'
# Border Line Set': [createBorderLineSet.1.Border Line Set.Invoke]'
def const_algBorderLineSet():
    return "createBorderLineSet"

## Polygon Set': [Polygon Set.ChildMenu.Polygon SetItem.1396441202]'
# Cleaned polygon surface': [createCleanedPolygonSet.1.Cleaned polygon surface.Invoke]'
def const_algCleanedPolygonSurface():
    return "createCleanedPolygonSet"

# Convex Hull polygon surface': [createConvexHullPolygonSet.1.Convex Hull polygon surface.Invoke]'
# def const_algConvexHullPolygonSurface():
#     return "createConvexHullPolygonSet"

# Patched polygon surface': [createPatchedPolygonSet.1.Patched polygon surface.Invoke]'
def const_algPatchedPolygonSurface():
    return "createPatchedPolygonSet"

# Simplified polygon surface': [createSimplifiedPolygonSet.1.Simplified polygon surface.Invoke]'
def const_algSimplifiedPolygonSurface():
    return "createSimplifiedPolygonSet"

# Value space mapped polygon surface': [createMappedPolygonSet.1.Value space mapped polygon surface.Invoke]'
def const_algValuespaceMappedPolygonSurface():
    return "createMappedPolygonSet"

## Polyline Set': [Polyline Set.ChildMenu.Polyline SetItem.1396441202]'
# Border Polyline Set': [createBorderPolylineSet.1.Border Polyline Set.Invoke]'
def const_algBorderPolylineSet():
    return "createBorderPolylineSet"

## Scalar Primitive Property': [Scalar Primitive Property.ChildMenu.Scalar Primitive PropertyItem.1396441202]'
# Scalar triangle info property': [createScalarTriangleInfoProperty.1.Scalar triangle info property.Invoke]'
def const_algScalarTriangleInfoProperty():
    #return "createScalarTriangleInfoProperty"
    return "Scalar triangle info property"

## Scalar Vertex Property': [Scalar Vertex Property.ChildMenu.Scalar Vertex PropertyItem.1396441202]'
# Scalar vertex info property': [createScalarVertexInfoProperty.1.Scalar vertex info property.Invoke]'
# def const_algScalarVertexInfoProperty():
#     return "createScalarVertexInfoProperty"

## Tetrahedron Set': [Tetrahedron Set.ChildMenu.Tetrahedron SetItem.1396441202]'
def const_tetrahedronSetContextMenu():
    return "Tetrahedron Set"

def const_deriveTetrahedronSet():
    return [const_algValuespaceMappedTetrahedronSet(),
        const_algMergedTetrahedronSet()]
    
# Value space mapped Tetrahedron Set': [createMappedTetrahedronSet.1.Value space mapped Tetrahedron Set.Invoke]'
def const_algValuespaceMappedTetrahedronSet():
    return "createMappedTetrahedronSet"

def const_algMergedTetrahedronSet():
    return "Merged tetrahedron set"

## Three-Component Primitive Property': [Three-Component Primitive Property.ChildMenu.Three-Component Primitive PropertyItem.1396441202]'
# Vector3 triangle info property': [createVector3TriangleInfoProperty.1.Vector3 triangle info property.Invoke]'
def const_algVector3TriangleInfoProperty():
    #return "createVector3TriangleInfoProperty"
    return "Three-component triangle info property"

## Three-Component Vertex Property': [Three-Component Vertex Property.ChildMenu.Three-Component Vertex PropertyItem.1396441202]'
# Vector3 vertex info property': [createVector3VertexInfoProperty.1.Vector3 vertex info property.Invoke]'
# def const_algVector3VertexInfoProperty():
#     return "createVector3VertexInfoProperty"

## Triangle Set': [Triangle Set.ChildMenu.Triangle SetItem.1396441202]'
# Cleaned triangle surface': [createCleanedTriangleSet.1.Cleaned triangle surface.Invoke]'
def const_algCleanedTriangleSurface():
    return "createCleanedTriangleSet"

# Convex Hull triangle surface': [createConvexHullTriangleSet.1.Convex Hull triangle surface.Invoke]'
# def const_algConvexHullTriangleSurface():
#     return "createConvexHullTriangleSet"

# Patched triangle surface': [createPatchedTriangleSet.1.Patched triangle surface.Invoke]'
def const_algPatchedTriangleSurface():
    return "createPatchedTriangleSet"

# Simplified triangle surface': [createSimplifiedTriangleSet.1.Simplified triangle surface.Invoke]'
def const_algSimplifiedTriangleSurface():
    #return "createSimplifiedTriangleSet"
    return "SimplifiedTriangleSet"

# Subset triangle surface': [createSubsetTriangleSet.1.Subset triangle surface.Invoke]'
def const_algSubsetTriangleSurface():
    return "createSubsetTriangleSet"

# Value space mapped triangle surface': [createMappedTriangleSet.1.Value space mapped triangle surface.Invoke]'
def const_algValueSpaceMappedTriangleSurface():
    return "createMappedTriangleSet"

# Sphere triangle surface
def const_algCreateSphereTriangleSurface():
    #return "createSphereTriangleSetInContainer"
    return "Sphere triangle surface"

def const_algSubdividedTriangleSet():
    return "createAndDefineSubdividedTriangleSet"

############<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Project tree constant object name  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def const_tabGeneral():
    return "General"

def const_tabLattice():
    return "Lattice"    
# def const_tabGeneralPetrel():
#     return "PTGeneral"

def const_tabCRS():
    return "CRS"
    
def const_tabInput():
    return "Input"

def const_tabBehavior():
    return "Behavior"

def const_tabBehaviorTS():
    return "BehaviorTS"

def const_tabOutput():
    return "Output"

def const_tabVisualization():
    return "Rendering"

def const_tabTwoWayVisualization():
    return "Corendering"

def const_tabParameters():
    return "Parameters"

def const_tabGeometry():
    return "Geometry"

def const_tabPlacement():
    return "Placement"

def const_tabInfo():
    return "Info"

def const_tabData():
    return "Data"

def constPickMore():
    return "ContinuePick*"

# derive 3D Prestack
# Cosine of Phase Prestack Volume
def const_algCosineOfPhasePrestack():
    return "DerivePrestackObjectHwCosineOfPhasePlugin"
# Dominant Frequency Prestack Volume
def const_algDominantFrequencyPrestack():
    return "DerivePrestackObjectHwDominantFrequencyPlugin"

# Envelope Prestack Volume
def const_algEnvelopePrestack():
    return "DerivePrestackObjectHwEnvelopePlugin"

# Instantaneous Bandwidth Prestack Volume
def const_algInstantaneousBandwidthPrestack():
    return "DerivePrestackObjectHwInstantaneousBandwidthPlugin"

# Instantaneous Frequency Prestack Volume
def const_algInstantaneousFrequencyPrestack():
    return "DerivePrestackObjectHwInstantaneousFrequencyPlugin"

# Instantaneous Phase Prestack Volume
def const_algInstantaneousPhasePrestack():
    return "DerivePrestackObjectHwInstantaneousPhasePlugin"

# Instantaneous Quality Prestack Volume
def const_algInstantaneousQualityPrestack():
    return "DerivePrestackObjectHwInstantaneousQualityPlugin"

# Quadrature Trace Prestack Volume
def const_algQuadratureTracePrestack():
    return "DerivePrestackObjectHwQuadratureTracePlugin"

# Sweetness Prestack Volume
def const_algSweetnessPrestack():
    return "DerivePrestackObjectHwSweetnessPlugin"

# Average Magnitude Prestack Volume
def const_algAverageMagnitudePrestack():
    return "DerivePrestackObjectHwAverageEnergyFilterPlugin"
    #return "DerivePrestackObjectHWReflectionIntensityPlugin"

# RMS Amplitude Prestack Volume
def const_algRMSAmplitudePrestack():
    return "DerivePrestackObjectHwRMSAmplitudeVolumePlugin"

# Reflection Intensity Prestack Volume
def const_algReflectionIntensityPrestack():
    return "DerivePrestackObjectHWReflectionIntensityPlugin"
    #return "DerivePrestackObjectHwAverageEnergyFilterPlugin"

# Bandpass Prestack Volume
def const_algBandpassPrestack():
    return "DerivePrestackObjectHwBandpassPlugin"

# First Derivative Prestack Volume
def const_algFirstDerivativePrestack():
    return "DerivePrestackObjectHWFirstDerivativePlugin"

# Math ?1 Attribute? Prestack Volume
def const_algMath1AttributePrestack():
    return "DerivePrestackObjectHwMathConstantFilterPlugin"

# Math (offset values) Prestack Volume
def const_algMathOffsetValuesPrestack():
    return "DerivePrestackObjectHwMathTraceHeaderFilterPlugin"

# Phase Shift Prestack Volume
def const_algPhaseShiftPrestack():
    return "DerivePrestackObjectHwPhaseShiftPlugin"

# Second Derivative Prestack Volume
def const_algSecondDerivativePrestack():
    return "DerivePrestackObjectHWSecondDerivativePlugin"

# Interpolate Prestack Volume
def const_algInterpolatePrestack():
    return "DerivePrestackObjectHWVolumeInterpolator"

# AGC Prestack Volume
def const_algAGCPrestack():
    return "DerivePrestackObjectHwTraceAGCPlugin"

# Linear Gain Prestack Volume
def const_algLinearGainPrestack():
    return "DerivePrestackObjectHwTimeGainFilterPlugin"

# Scalar Gain Prestack Volume
def const_algScalarGainPrestack():
    return "DerivePrestackObjectHwScalarGainFilterPlugin"

# T-Squared Gain Prestack Volume
def const_algTSquaredGainPrestack():
    return "DerivePrestackObjectHwTSquareGainFilterPlugin"

# Trace Balance Prestack Volume
def const_algTraceBalancePrestack():
    return "DerivePrestackObjectHwTraceBalancingPlugin"

# Model Radon Prestack Volume
def const_algModelRadonPrestack():
    return "DerivePrestackObjectHwModelRadonPlugin"

# Radon Transform Prestack Volume
def const_algRadonTransformPrestack():
    return "DerivePrestackObjectHwRadonPlugin"

# Extract trace Poststack Volume
def const_algExtractTracePoststack():
    return "DerivePoststackObjectExtractTrace"

# Mute Prestack Volume
def const_algMutePrestack():
    return "DerivePrestackObjectHwMuteFilterPlugin"

# Peak Pick Poststack Volume
def const_algPeakPickPoststack():
    return "DerivePoststackObjectHwPeakPick"

# Stack Poststack Volume
def const_algStackPoststack():
    return "DerivePoststackObjectHwStackFilterPlugin"

# Supergather Prestack Volume
def const_algSupergatherPrestack():
    return "DerivePrestackObjectHwSuperGathersPlugin"

# Trim Statics Prestack Volume
def const_algTrimStaticsPrestack():
    return "DerivePrestackObjectHwTrimStaticsPlugin"

# Create Synthetic VDS Prestack Volume
def const_algCreateSyntheticVDSPrestack():
    return "DerivePrestackObjectHwCreateSyntheticVDSPlugin"

# Create Vertical Sine Wave Prestack Volume
def const_algCreateVerticalSineWavePrestack():
    return "DerivePrestackObjectHwCreateVerticalSineWave"

# NEW - Math ?1 Attribute? Prestack Volume
def const_algMath1AttributeNEWPrestack():
    return "DerivePrestackObjectHwMathConstantFilterPlugin2"

# NEW - Stack Poststack Volume
def const_algNEWStackPoststack():
    return "DerivePoststackObjectHwSTCKR"

# Pseudo azimuth gather Prestack Volume
def const_algPseudoAzimuthGatherPrestack():
    return "DerivePrestackObjectHwAzimuthGatherPlugin"

# Create Velocity Field Poststack Volume
def const_algCreateVelocityFieldPoststack():
    return "DerivePoststackObjectHwNMOVelocityFilterPlugin"

# Semblance Prestack Volume
def const_algSemblancePrestack():
    return "DerivePrestackObjectHwSemblancePlugin"

# Directional convolution Prestack Volume
def const_algDirectionalConvolutionPrestack():
    return "DerivePrestackObjectHWConvolution1DPrestackPlugin"

# Offset Azimuth Prestack Volume
def const_algOffsetAzimuthPrestack():
    return "DerivePrestackObjectHwWAZResamplerPlugin"

#~~~~~~~~~~~~~~~~~~~~~ #3D Post stack ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Cosine of Phase Poststack Volume
def const_algCosineOfPhasePoststack():
    return "DerivePoststackObjectHwCosineOfPhasePlugin"

# Dominant Frequency Poststack Volume
def const_algDominantFrequencyPoststack():
    #return "DerivePoststackObjectHwDominantFrequencyPlugin"
    return "DominantFrequency"
# Envelope Poststack Volume
def const_algEnvelopePoststack():
    return "DerivePoststackObjectHwEnvelopePlugin"

# Instantaneous Bandwidth Poststack Volume
def const_algInstantaneousBandwidthPoststack():
    return "DerivePoststackObjectHwInstantaneousBandwidthPlugin"

# Instantaneous Frequency Poststack Volume
def const_algInstantaneousFrequencyPoststack():
    return "DerivePoststackObjectHwInstantaneousFrequencyPlugin"

# Instantaneous Phase Poststack Volume
def const_algInstantaneousPhasePoststack():
    return "DerivePoststackObjectHwInstantaneousPhasePlugin"

# Instantaneous Phase Quality Volume
def const_algInstantaneousQualityPoststack():
    return "DerivePoststackObjectHwInstantaneousQualityPlugin"

# Quadrature Trace Poststack Volume
def const_algQuadratureTracePoststack():
    return "DerivePoststackObjectHwQuadratureTracePlugin"

# Sweetness Poststack Volume
def const_algSweetnessPoststack():
    return "DerivePoststackObjectHwSweetnessPlugin"

# Dilate Erode Filter Poststack Volume
def const_algDilateErodeFilterPoststack():
    return "DerivePoststackObjectHwDilateErodeFilterPlugin"

# Average Magnitude Poststack Volume
#def const_algAverageMagnitudePoststack():
#    return "DerivePoststackObjectHWReflectionIntensityPlugin"

# RMS Amplitude Poststack Volume
def const_algRMSAmplitudePoststack():
    return "DerivePoststackObjectHwRMSAmplitudeVolumePlugin"

# Reflection Intensity Poststack Volume
def const_algReflectionIntensityPoststack():
    return "DerivePoststackObjectHWReflectionIntensityPlugin"

def const_algAverageMagnitudePoststack():    
    return "DerivePoststackObjectHwAverageEnergyFilterPlugin"

# Bandpass Poststack Volume
def const_algBandpassPoststack():
    return "DerivePoststackObjectHwBandpassPlugin"

# First Derivative Poststack Volume
def const_algFirstDerivativesPoststack():
    return "DerivePoststackObjectHWFirstDerivativePlugin"

# Math ?1 Attribute? Poststack Volume
def const_algMath1AttributePoststack():
    return "DerivePoststackObjectHwMathConstantFilterPlugin"

# Math 1 Attribute 2D Prestack Gather Line
def const_algMath1Attribute2DPrestackGatherLine():
    return "DeriveGathers2DLineObjectHwMathConstantFilterPlugin"

# Phase Shift Poststack Volume
def const_algPhaseShiftPoststack():
    return "DerivePoststackObjectHwPhaseShiftPlugin"

# Second Derivative Poststack Volume
def const_algSecondDerivativePoststack():
    return "DerivePoststackObjectHWSecondDerivativePlugin"

# Resampled Poststack Object
def const_algResampledPoststack():
    return "DeriveResampledPoststackObject"

# Interpolate Poststack Volume
def const_algInterpolatePoststack():
    return "DerivePoststackObjectHWVolumeInterpolator"

# AGC Poststack Volume
def const_algAGCPoststack():
    return "DerivePoststackObjectHwTraceAGCPlugin"

# Linear Gain Poststack Volume
def const_algLinearGainPoststack():
    return "DerivePoststackObjectHwTimeGainFilterPlugin"

# Scalar Gain Poststack Volume
def const_algScalarGainPoststack():
    return "DerivePoststackObjectHwScalarGainFilterPlugin"

# T-Squared Gain Poststack Volume
def const_algTSquaredGainPoststack():
    return "DerivePoststackObjectHwTSquareGainFilterPlugin"

# Trace Balance Poststack Volume
def const_algTraceBalancePoststack():
    return "DerivePoststackObjectHwTraceBalancingPlugin"

# Decimate Poststack Volume
def const_algDecimatePoststack():
    return "DerivePoststackObjectHwDecimatePoststackPlugin"

# Create Vertical Sine Wave Poststack Volume
def const_algCreatereateVerticalSineWavePoststack():
    return "DerivePoststackObjectHwCreateVerticalSineWave"

# Create Synthetic VDS Poststack Volume
def const_algCreateSyntheticVDSPoststack():
    return "DerivePoststackObjectHwCreateSyntheticVDSPlugin"

# Implicit Merge Poststack Volume
def const_algImplicitMergePoststack():
    return "DerivePoststackObjectImplicitMerge"

# NEW - Math ?1 Attribute? Poststack Volume
def const_algMath1AttributeNEWPoststack():
    return "DerivePoststackObjectHwMathConstantFilterPlugin2"

# Steerable filter (oriented 2D convolution) Poststack Volume
def const_algSteerableFilterPoststack():
    return "DerivePoststackObjectHWSteerFilterPlugin"
#
def const_algSteerableFilter4DPrestack():
    return "DerivePrestackObjectHWSteerFilterMultiAng4DPlugin"
# S Transform Poststack Volume
def const_algSTransformPoststack():
    return "DerivePoststackObjectHwFastSpectralDecomp"

# Create Velocity Field Poststack Volume - exists on prestack
# def const_algCreateVelocityFieldPoststack():
#     return "DerivePoststackObjectHwNMOVelocityFilterPlugin"

# Velocity Conversions in time Poststack Volume
def const_algVelocityConversionsInTimePoststack():
    return "DerivePoststackObjectHwVelocityConversionsPlugin"

# Vertical Smooth Poststack Volume
def const_algVerticalSmoothPoststack():
    return "DerivePoststackObjectHwSmoothPlugin"

def const_algThinFaultLikelyHoodsPoststack():
    return "Thin fault likelyhoods Poststack Volume"
#~~~~~~~~~~~~~~~~~~~~~ #Horizon ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Math ?1 Attribute? Poststack Horizon
def const_algMath1AttributePoststackHorizon():
    return "DeriveHorizonObjectHwMathConstantFilterPlugin"

# Resampled Horizon Object
def const_algResampledHorizonObject():
    return "DeriveResampledHorizonObject"

# Interpolate Poststack Horizon
def const_algInterpolatePoststackHorizon():
    return "DeriveHorizonObjectHWVolumeInterpolator"

# Horizon Smooth Poststack Horizon
def const_algHorizonSmoothPoststackHorizon():
    return "DeriveHorizonObjectHwHorizonSmoothingPlugin"

# NEW - Math ?1 Attribute? Poststack Horizon
def const_algMathAttributeNEWPoststackHorizon():
    return "DeriveHorizonObjectHwMathConstantFilterPlugin2"
# Clean edges and fill holes
def const_algCleanEdgesAndHillHoles():
    return "FillHolesAction"

def const_algHorizonHoleFill():
    return "HorizonHoleFiller"

def const_algExtendToEdgeAndFill():
    return "Extend to edge and fill" 

def const_horizonAttribute1Viz():
    return "TargetObject1"

def const_keyDefaultAttributeCount():
    return "DefaultAttributeCount"

def const_key3DRegion():
    return "DefaultRegion3D"

def const_keyBottomOffset():
    return "BottomOffset"

def const_algHorizonInfill():
    return "Horizon Infill"

def const_algHorizonAttributeFromPoststack():
    return "HWHorizonAttributeFromPoststack"

def const_algHorizonAttributeFromVerticalFunction():
    return "Horizon attribute from vertical function"

def const_algHorizonCleanEdgesFillHoles():
    return "FillHolesAction"

def const_pickMore():
    return "Continue picking horizon"

#~~~~~~~~~~~~~~~~~~~~~ #Horizon x Horizon ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Math (2 Attributes) Poststack Horizon
def const_algMath2AttributesPoststackHorizon():
    return "Math*2*ttributes*oststack*orizon"

# Interpolate Poststack Horizon
def const_algInterpolatePoststack2Horizons():
    return "Interpolate Poststack Horizon"

#    Radius and Azimuth Poststack Horizon
def const_algRadiusAndAzimuthPoststack2Horizons():
    return "Radius and Azimuth Poststack Horizon"

#~~~~~~~~~~~~~~~~~~~~~ # Prestack x Velocity/post stack~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Interpolate Poststack Volume (2 inputs)
def const_algInterpolatePoststack2Inputs():
    return "Interpolate Poststack Volume"

# Interpolate Prestack Volume (2 inputs)
def const_algInterpolatePrestack2Inputs():
    return "Interpolate Prestack Volume"

# Radius and Azimuth Prestack Volume
def const_algRadiusandAzimuthPrestackVolume2Inputs():
    return "Radius and Azimuth Prestack Volume"

#Offset to Angle Prestack Volume
def const_algOffsetToAnglePrestack2Inputs():
    return "DerivePrestackObjectHwOffsetToAngleFilterPluginTwoInputs"

def const_algAngleMutePrestackVolume():
    return "DerivePrestackObjectHWAngleMuteTwoInputsInputsFlipped"

# "AVO Attributes Poststack Volume",
def const_algAVOAttributesPoststack():
    return "DerivePoststackObjectHwAVOAttributesFilterPluginTwoInputs"

# NMO correction Prestack Volume
def const_algNMOCorrectionPrestack():
    #return "DerivePrestackObjectHwTimeVariantNMOFilterPluginTwoInputs"
    return "NMOCorrect"

# Velocity Scalar Prestack Volume
def const_algVelocityScalarPrestack():
    return "DerivePrestackObjectHwVelocityScanFilterPluginTwoInputs"

def    const_keyVelocityScanMin():
    return "velocityScanMin"

def    const_keyVelocityScanMax():
    return "velocityScanMax"

def    const_keyVelocityScanStep():
    return "velocityScanStep"

def    const_keyStretchFactor():
    return "stretchFactor"

def    const_keyHalfWindowLength():
    return "halfWindowLength"

def const_keyAngleStart():
    return "firstAngle"

def const_keyAngleIncrement():
    return "angleInterval"

def const_keyAngleEnd():
    return "lastAngle"

def const_keyAngleMute():
    return "angleValue"

def const_keyFrequencyMin():
    return "hzMin"

def const_keyFrequencyMax():
    return "hzMax"

def const_keyFrequencyStep():
    return "hzStep"

def const_keyVDSProduceStatus01():
    return "VDSProduceStatus01"

def const_keyVDSProduceStatus02():
    return "VDSProduceStatus02"

def const_keyVDSProduceStatus12():
    return "VDSProduceStatus12"

def const_keyVDSProduceStatus012():
    return "VDSProduceStatus012"

def const_keyVDSProduceStatus013():
    return "VDSProduceStatus013"

def const_keyVDSProduceStatus023():
    return "VDSProduceStatus023"

def const_keyVDSProduceStatus():
    return "VDSProduceStatus"

def const_keyVelocityFieldPercent():
    return "percentValue"

# un-group alg

def const_algCreateBlendingForPoststack():
    #return "CreateCoRenderInstancePoststack*Blend"
    return "CreateCoRender*Blend"
    

def const_algCreateBlendingForInline():
    return "CreateCoRender*InstanceInlineSlice*Blend"

def const_algCreateBlendingForVolume():
    return "*CreateRenderInstance*Blend*"

def const_algVelocityConversionsInTimePoststackObject():
    return "DerivePoststackObjectHwVelocityConversionsPlugin"

def const_algVelocityConversionsInDepthPoststackVolume():
    return "Velocity Conversions in depth Poststack Volume"

def const_algVolumeTimeToDepthPoststackObject():
    return "Volume time-to-depth Poststack Volume"

def const_algVolumeTimeToDepthPrestackObject():
    return "DerivePrestackObjectHwTimeDepthConversionPluginTwoInputs"

def const_algSeismicLineTimeToDepth():
    return "Seismic line time-to-depth"
#     return "HWSeismicLineTime2Depth"

def const_algSeismicLineDepthToTime():
    return "Seismic line depth-to-time"
#     return "HWSeismicLineDepth2Time"

def const_algSeismicLineTimeToDepthExtend():
    return "Seismic line time-to-depth..."

def const_algSeismicLineDepthToTimeExtend():
    return "Seismic line depth-to-time..."
   
def const_algDomainConverterPrestack():
    return "DerivePrestackObjectHwDomainConverterPlugin"

def const_algDomainConverterPoststack():
    return "DerivePoststackObjectHwDomainConverterPlugin"

def const_algVolumeDepthToTimePrestackObject():
    return "Volume depth-to-time Prestack Volume"

def const_algMath2AttributesPrestackHorizon():
    return "Math*2*ttributes*restack*"

def const_algHorizonTimeToDepthPoststackHorizon():
    return "Horizon time-to-depth Poststack Horizon"

def const_algDomainConverterPoststackHorizon():
    return "DeriveHorizonObjectHwDomainConverterPluginTwoInputs"

# def const_algNMOCorrectionPrestackDataset():
#     return "DerivePrestackObjectHwTimeVariantNMOFilterPluginTwoInputsInputs"

def const_algMath2Attributes2DPrestackGatherLine():
    return "Math*2*ttributes*2D*restack*"

def const_algMath2Attributes2DPoststackLine():
    return "Math*2*ttributes*2D*oststack*"

def const_algMath2AttributesPoststackVolume():
    return "Math*2*ttributes*oststack*"

# Interpolate Poststack Volume
def const_algInterpolatePoststackVolume2Inputs():
    return "Interpolate Poststack Volume"

# Radius and Azimuth Poststack Volume
def const_algRadiusandAzimuthPoststackVolume2Inputs():
    return "Radius and Azimuth Poststack Volume"

def const_algMinimalDistancePoststackVolume():
    return "MinimalDistance Poststack Volume"

def const_algMath2AttributesPrestackVolume():
    return "Math*2*ttributes*restack*" 

def const_algResampleFilterPrestackVolume():
    return "Resample Filter Prestack Volume"

def const_algHwVDSTravelTimeSkeletonPrestackVolume():
    return "HwVDSTravelTimeSkeleton Prestack Volume"

# prestack x postack
# Interpolate Prestack Horizon
def const_algInterpolatePrestackHorizon2Inputs():
    return "DerivePrestackHorizonObjectHWVolumeInterpolatorTwoInputsInputs"
# Interpolate Prestack Volume'
def const_algInterpolatePrestackVolume2Inputs():
    return "DerivePrestackObjectHWVolumeInterpolatorTwoInputs"

# Wide Azimuth Combine
def const_algWideAzimuthCombine():
    return "HWWAZCombiner"

# def const_dictDeriredCombineName():
#     list = const_coreAttributesInstantaneousGroupAlgorithm()
#     dict = {
#             "Velocity Conversions in time Poststack Volume":'[Velocity Conversions in time]',
#             "Velocity Conversions in depth Poststack Volume":'[Velocity Conversions in depth]',
#             "Volume time-to-depth Poststack Volume":'[Volume time-to-depth]',
#             "DerivePrestackObjectHwTimeDepthConversionPluginTwoInputsInputsFlipped":'[Volume time-to-depth]',
#             "Volume depth-to-time Prestack Volume":'[Volume depth-to-time]',
#             const_algInterpolatePoststackHorizon():'[Interpolate Poststack]',
#             "Math *2 Attributes* Poststack Horizon":'[Math *2 Attributes*]',
#             "Horizon time-to-depth Poststack Horizon":'[Horizon time-to-depth]',
#             "DerivePrestackObjectHwTimeVariantNMOFilterPluginTwoInputsInputsFlipped":'[NMO correction]',
#             "Volume depth-to-time Poststack Volume":'[Volume depth-to-time]',
#             "Math ?1 Attribute? Poststack Volume":'[Math ?1 Attribute?]',
#             "Horizon time-to-depth Poststack Horizon":'[Horizon time-to-depth]',
#             "Horizon depth-to-time Poststack Horizon":'[Horizon depth-to-time]',
#             "Offset to Angle Prestack Volume":'[Offset to Angle]',
#             "Angle Gathers Prestack Volume":'[Angle Gathers]',
#             "Math *2 Attributes* Prestack Volume":'[Math *2 Attributes*]',
#             "Math *2 Attributes* 2D Poststack Line":'[Math *2 Attributes*]',
#             "Math *2 Attributes* 2D Prestack Gather Line":'[Math *2 Attributes*]',
#             "Math *2 Attributes* Poststack Volume":'[Math *2 Attributes*]'
#             }
#     return dict

def const_algVolumeDepthToTimePoststackObject():
    return "Volume depth-to-time Poststack Volume"

def const_algMath1AttributePoststackVolume():
    return "Math*1*ttribute*oststack*"

def const_algDirectionalSmoothPoststackVolume():
    return "Directional Smooth Poststack Volume"

def const_algFaultScannerPoststackVolume():
    return "Fault Scanner Poststack Volume"

def const_algGaussionFilterPoststackVolume():
    return "FGaussion Filter Poststack Volume"

def const_algSlopesPoststackVolume():
    return "Slopes Poststack Volume"

def const_filterAndOperationAlgorithmContextMenu():
    return "Filters and Operations"

def const_dataEnhancementContextMenu():
    return "FIX"

def const_HwOnlyUseContextMenu():
    return "Hw Only Use"
def const_SyntheticDataContextMenu():
    return "Synthetic Data"

def const_AlphaStageContextMenu():
    return "Alpha Stage"

def const_coreContextMenu():
    return "Core"

def const_frameContextMenu():
    return "Frame"

def const_T2DModuleContextMenu():
    return "T2D Module"

def const_domainConversionContextMenu():
    return "Domain conversion"

def const_velocityVerticalFunctionSet():
    return "Velocity vertical function set"

def const_wideAzimuthContextMenu():
    return "Wide azimuth"

def const_wideazimuthContextMenu():
    return "Wide azimuth"

def const_forValidationContextMenu():
    return "For Validation"

def const_avoAnalysisContextMenu():
    return "AVO Analysis"

def const_SQIContextMenu():
    return "SQI"

def const_SqiContextMenu():
    return "Sqi"

def const_spectralDecompositionContextMenu():
    return "Spectral Decomposition"

def const_interpolatePoststackVolumeContextMenu():
    return "Interpolate Poststack Volume"


##################################### FileName in DataSet #################################
def const_file_4dmig_rms_vel_t():
    return "4dmig_rms_vel_t"

def const_file_VINT_IN_TIME_CORRECT_xy():
    return "VINT_IN_TIME_CORRECT_xy"

def const_file_Piceance_3D_depthVol():
    return "Piceance_3D_depthVol"

def const_file_Hoover_Vrms():
    return "Hoover_Vrms"

def const_file_Wintershall_Finvel():
    return "Finvel"

def const_file_D05_Y_MIGINPUT_CMPGTHRS_HMM05():
    return "D05_Y_MIGINPUT_CMPGTHRS_HMM05"

def const_file_Hoover_gathers():
    return "Hoover_gathers"

def const_file_Hoover05APSDMFullStack():
    return "Hoover 05 APSDM Full Stack"

def const_file_Wintershall_STB02132_14_19_stk():
    return "STB02132_14-19_stk"

def const_file_Wintershall_Horizon():
    return "Horizon_01"

def const_file_A_angle_0_30degree_stack_FF04_01():
    return "A_angle_0-30degree_stack_FF04_01"

def const_file_PostMigration_CDP_NMO_FF04_01_031314():
    return "PostMigration_CDP_NMO_FF04_01_031314"
###################################### Headwave Algorithms Name ###########################
def const_deriveContextMenu():
    return "Derive."

def const_deriveConbinedContextMenu():
    return "Derive combined"

def const_createMenuItem():
    return "Create"

def const_removeMenuItem():
    return "Remove"

def const_algHorizonTimeToDepthPoststackObject():
    return "Horizon time-to-depth Poststack Horizon"

def const_algHorizonDepthToTimePoststackObject():
    return "Horizon depth-to-time Poststack Horizon"

def const_algOffsettoAnglePrestackVolume():
    return "DerivePrestackObjectHwOffsetToAngleFilterPluginTwoInputs" #Offset to Angle Prestack Volume

def const_algAngleGathersPrestackVolume():
    return "DerivePrestackObjectHwAngleGathersPluginTwoInputs" #Angle Gathers Prestack Volume

def const_algExtractTracePoststackHorizon():
    return "DeriveHorizonObjectExtractTrace"

def const_algExtractFixedTraceHorizon():
    return "ExtractFixedTraceHorizon"


# def const_algMath1AttributeHorizon():
#     return "DeriveHorizonObjectHwMathConstantFilterPlugin"

# def const_algMath2AttributeHorizon():
#     return "Math *2 Attributes* Poststack Horizon"

# def const_algHorizonInterpolationPoststackHorizon():
#     return "DeriveHorizonObjectHWVolumeInterpolator"

# def const_algResample2Horizon():
#     return "DeriveResampledHorizonObject"
#
# def const_algResampledPoststackObject():
#     return "DeriveResampledPoststackObject"

# def const_algHorizonSmooth():
#     return "DeriveHorizonObjectHwHorizonSmoothingPlugin"

def const_algOffsetAzimuthPrestackVolume():
    return "Offset/Azimuth subsetting Prestack Volume"

# def const_algStackPoststackVolume():
#     return "DerivePoststackObjectHwStackFilterPlugin"
#############################################################################################################

# def const_algPoststackObjectHwPeakPickDerive():
#     return "DerivePoststackObjectHwPeakPick"
#
# def const_algVericalSmoothPoststack():
#     return "DerivePoststackObjectHwSmoothPlugin"

# def const_algOffset2AnglePrestack():# display text -> Offset to Angle Prestack Volume
#     return "DerivePrestackObjectHwOffsetToAngleFilterPluginTwoInputsInputsFlipped"

def const_algAngleGatherPrestack():# display text -> Angle Gathers Prestack Volume
    return "DerivePrestackObjectHwAngleGathersPluginTwoInputs"

#############################################################################################################

#############################################################################################################

def const_algPoststackCLSSAPrestack():
    return "DerivePrestackObjectHwCLSSA" #"CLSSA Prestack Volume"

#############################################################################################################

########################Group name of newly created derivative ##############################################
def const_menuCreate():
    #return "Create*ChildMenu"
    return "Create"

def const_menuDeriveCombined():
    return "Derive Combined"

def const_menuDerive():
    return "Derive"

def const_menuItemDelete():
    #return "ObjectActionDelete"
    return "Delete*Delete"

def const_menuExport():
    return "Export*ChildMenu"

def const_menuExportPointsetSmf():
    return "HWPointsetExporters"

def const_menuExportTriangleSurfaceSmf():
    return "HWShapeExporters"

def const_menuGroups():
    return "Misc*Groups"

def const_menuLinkedGroup():
    return "Linked"

def const_algMath1AttributeName():
    return "*Math*1*ttribute*"

def const_algMath2AttributeHorizonName():
    return "*Math*2*ttributes*"

def const_menuItemGatherTracker():
    return "PrestackHorizonAutotracker"

def const_menuItemSTFT():
    return "Stft poststack volume"

def const_menuItemCreateInlineHorizon():
    return "InstantiatePrestackHorizonInlineObject"

def const_menuItemCreateCrosslineHorizon():
    return "InstantiatePrestackHorizonCrosslineObject"

def const_menuItemCreateTraceHorizon():
    return "InstantiatePrestackHorizonTraceObject"

def const_menuItemAttribute1():
    return "TargetObject1"

def const_menuItemMarkerMistieAttribute():
    return "HorizonMistieAttribute"

def const_algMergeHorizons():
    return "Merge*oststack*orizon*"

def const_menuSeismicAttributes():
    return "Seismic Attributes"

############################# Interpretation ##############################################
def const_algHorizonFromShape():
    return "HWHorizonFromShapePlugin"

########################Group core algorithm ##############################################
def const_coreAttributesInstantaneousGroupAlgorithm():
    return [
            
            #const_algInstantaneousBandwidthPoststack(),
            #const_algInstantaneousFrequencyPoststack(),
            #const_algInstantaneousPhasePoststack(),
            #const_algInstantaneousQualityPoststack(),
            #const_algQuadratureTracePoststack(),
            #const_algSweetnessPoststack(),
#              "DerivePoststackObjectHWReflectionIntensityPlugin",
            #const_algCosineOfPhasePrestack(),
            #const_algDominantFrequencyPrestack(),
            #const_algEnvelopePrestack(),
            #const_algInstantaneousBandwidthPrestack(),
            #const_algInstantaneousFrequencyPrestack(),
            #const_algInstantaneousPhasePrestack(),
            #const_algInstantaneousQualityPrestack(),
            #const_algQuadratureTracePrestack(),
            #const_algSweetnessPrestack()
            ]
    
def const_frameGroupAlgorithm():
    return [const_algMergeHorizons(),
           const_algHorizonSmoothPoststackHorizon(),
           const_algHorizonHoleFill()
           ]

def const_frameDeprecatedGroupAlgorithm():
    return [
           const_algCleanEdgesAndHillHoles(),
           const_algExtendToEdgeAndFill(),
           const_algHorizonInfill()
           ]

# def const_coreAttributesInstantaneousGroupAlgorithmCreatedDerivativeName():
#     return ["DerivePoststackObjectHwCosineOfPhasePlugin",     
#             "DerivePoststackObjectHwDominantFrequencyPlugin",
#             "DerivePoststackObjectHwEnvelopePlugin",
#             "DerivePoststackObjectHwInstantaneousBandwidthPlugin",
#              "DerivePoststackObjectHwInstantaneousFrequencyPlugin",
#              "DerivePoststackObjectHwInstantaneousPhasePlugin",
#              "Instantaneous Quality Poststack Volume",
#              "Quadrature Trace Poststack Volume",
#              "Sweetness Poststack Volume"
#              "Cosine of Phase Prestack Volume",
#             "Dominant Frequency Prestack Volume",
#             "Envelope Prestack Volume",
#             "Instantaneous Bandwidth Prestack Volume",
#              "Instantaneous Frequency Prestack Volume",
#              "Instantaneous Phase Prestack Volume",
#              "Instantaneous Quality Prestack Volume",
#              "Quadrature Trace Prestack Volume",
#              "Sweetness Prestack Volume"
#             ]    
    
# def const_dictCoreAttributesInstantaneousGroupAlgorithm():
#     list = const_coreAttributesInstantaneousGroupAlgorithm()
#     dict = {
#             list[0]:'[Cosine of Phase]',
#             list[1]:'[Dominant Frequency]',
#             list[2]:'[Envelope]',
#             list[3]:'[Instantaneous Bandwidth]',
#             list[4]:'[Instantaneous Frequency]',
#             list[5]:'[Instantaneous Phase]',
#             list[6]:'[Instantaneous Quality]',
#             list[7]:'[Quadrature Trace]',
#             list[8]:'[Sweetness]',
#             list[9]:'[Cosine of Phase]',
#             list[10]:'[Dominant Frequency]',
#             list[11]:'[Envelope]',
#             list[12]:'[Instantaneous Bandwidth]',
#             list[13]:'[Instantaneous Frequency]',
#             list[14]:'[Instantaneous Phase]',
#             list[15]:'[Instantaneous Quality]',
#             list[16]:'[Quadrature Trace]',
#             list[17]:'[Sweetness]'
#             }
#     return dict
    
def const_coreAttributesMultiTraceWindowedGoupAlgorithm():
    return [
            ]
    
def const_dictCoreAttributesMultiTraceWindowedGoupAlgorithm(): #prestack
    dict = {
            const_algDilateErodeFilterPoststack():'[Dilate Erode Filter]',
            }
    return dict
#         
        
def const_coreAttributesWindowedGoupAlgorithm():
    return [const_algReflectionIntensityPoststack(),
            const_algAverageMagnitudePrestack(),
            const_algRMSAmplitudePrestack(),
            const_algReflectionIntensityPrestack()
            ]    

# def const_dictCoreAttributesWindowedGoupAlgorithm():
#     list = const_coreAttributesWindowedGoupAlgorithm()
#     dict = {
#             list[0]:'[Average Magnitude]',
#             list[1]:'[RMS Amplitude]',
#             list[2]:'[Reflection Intensity]',
#             list[3]:'[Average Magnitude]',
#             list[4]:'[RMS Amplitude]',
#             list[5]:'[Reflection Intensity]'
#             }
#     return dict    

def const_hwOnlyUseFiltersAndOperationGroupAlgorithm():
    return [const_algBandpassPoststack(),
        ]        

def const_groupFIXSeismicAttributes():
    return [
            # For poststack
            const_algAverageMagnitudePoststack(),
            const_algCosineOfPhasePoststack(),
            const_algDominantFrequencyPoststack(),
            const_algEnvelopePoststack(),
            const_algFirstDerivativesPoststack(),
            const_algInstantaneousBandwidthPoststack(),
            const_algInstantaneousFrequencyPoststack(),
            const_algInstantaneousPhasePoststack(),
            const_algInstantaneousQualityPoststack(),
            const_algRMSAmplitudePoststack(),
            const_algReflectionIntensityPoststack(),
            const_algSecondDerivativePoststack(),
            const_algSweetnessPoststack(),
            
            # For Prestack        
            const_algAverageMagnitudePrestack(),    
            const_algCosineOfPhasePrestack(),
            const_algDominantFrequencyPrestack(),
            const_algEnvelopePrestack(),
            const_algFirstDerivativePrestack(),
            const_algInstantaneousBandwidthPrestack(),
            const_algInstantaneousFrequencyPrestack(),
            const_algInstantaneousPhasePrestack(),
            const_algInstantaneousQualityPrestack(),
            const_algRMSAmplitudePrestack(),
            const_algReflectionIntensityPrestack(),
            const_algSecondDerivativePrestack(),
            #const_algQuadratureTracePrestack(),
            const_algSweetnessPrestack(),
            
            
                    
           ]

def const_coreFiltersAndOperationGroupAlgorithm():
    return [const_algMath1AttributePoststack(),
            const_algMath1AttributePoststackHorizon(),
            const_algMath2AttributesPoststackHorizon(),
            const_algMath2Attributes2DPrestackGatherLine(),
            const_algMath2Attributes2DPoststackLine(),
            const_algMath2AttributesPoststackVolume(),
            const_algMath2AttributesPrestackVolume(),
            const_algResampleFilterPrestackVolume(),
            const_algMinimalDistancePoststackVolume(),
            #const_algBandpassPrestack(),
            const_algMath1AttributePrestack(),
            const_algMathOffsetValuesPrestack(),
            #const_algPhaseShiftPrestack(),
            const_algMath1Attribute2DPrestackGatherLine(),
            const_algExtractFixedTraceHorizon()
        ]    
    
# def const_dictCoreFiltersAndOperationGroupAlgorithm():
#     list = const_coreFiltersAndOperationGroupAlgorithm()
#     dict = {
#             list[0]:'[Bandpass]',
#             list[1]:'[First Derivative]',
#             list[2]:'[Math ?1 Attribute?]',
#             list[3]:'[Math (offset values)]',
#             list[4]:'[Phase Shift]',
#             list[5]:'[Second Derivative]',
#             list[6]:'[Bandpass]',
#             list[7]:'[First Derivative]',
#             list[8]:'[Math ?1 Attribute?]',
#             list[9]:'[Phase Shift]',
#             list[10]:'[Second Derivative]',
#             list[11]:'[Math (2 Attribute]',
#             list[12]:'[Math ?1 Attribute?]',
#             list[13]:'[Math ?2 Attribute?]'
#             }
#     return dict        
#         

def const_coreAlgorithmGroup():
    return [#const_algResampledPoststack(),
            #const_algResampledHorizonObject(),
            const_algExtractTracePoststack(),        
            const_algHorizonAttributeFromPoststack(),
            const_algHorizonFromShape()
            ]    
    
# def const_dictCoreAlgorithmGroupAlgorithm():
#     list = const_coreAlgorithmGroup()
#     dict = {
#             list[0]:'[Resample]',
#             list[1]:'[Resample]'
#             }
#     return dict        
    
def const_dataEnhancementFiltersAndOperationsGroupAlgorithm():
    return [
#         const_algInterpolatePoststack(),
#             const_algInterpolatePrestack(),
        ]    

def const_coreInterpolation():
    return [
            const_algInterpolatePoststackVolume2Inputs(),
            const_algInterpolatePoststack2Horizons(),
            const_algInterpolatePoststack2Inputs(),
            const_interpolatePoststackVolumeContextMenu(),        
            const_algInterpolatePoststackHorizon(),
            const_algInterpolatePrestack2Inputs(),
            const_algInterpolatePrestackVolume2Inputs(),
            const_algInterpolatePrestackHorizon2Inputs(),
            const_algInterpolatePoststack()            
        ]

def const_coreHorizonGeometry():
    return [
            const_algDeriveHorizonTriangleSurface(),
            const_algDeriveHorizonPointSurface()    
        ]
    
def const_onlyHWUsesyntheticDataGroupAlgorithm():
    return [const_algCreateSyntheticVDSPoststack(),
            const_algCreatereateVerticalSineWavePoststack(),
            const_algCreateSyntheticVDSPrestack(),
            const_algCreateVerticalSineWavePrestack(),
        ]    

def const_AlphaStageGroupAlgorithm():
    return [const_algPseudoAzimuthGatherPrestack()]
        
# def const_dictDataEnhancementFiltersAndOperationsGroupAlgorithm():
#     list = const_dataEnhancementFiltersAndOperationsGroupAlgorithm()
#     dict = {
#             list[0]:'[Interpolate]',
#             list[1]:'[Interpolate]',
#             list[2]:'[Interpolate]',
#             }
#     return dict    

def const_dataEnhancementGainGroupAlgorithm():
    return [const_algAGCPoststack(),
            const_algLinearGainPoststack(),
            const_algScalarGainPoststack(),
            const_algTSquaredGainPoststack(),
            const_algTraceBalancePoststack(),
            
            const_algAGCPrestack(),
            const_algLinearGainPrestack(),
            const_algScalarGainPrestack(),
            const_algTSquaredGainPrestack(),
            const_algTraceBalancePrestack()

        ]

def const_dataEnhancementRadonGroupAlgorithm():
    return [const_algModelRadonPrestack(),
            const_algRadonTransformPrestack()
        ]
    
            
            
# def const_dictDataEnhancementGainGroupAlgorithm():
#     list = const_dataEnhancementGainGroupAlgorithm()
#     dict = {
#             list[0]:'[AGC]',
#             list[1]:'[Linear Gain]',
#             list[2]:'[Scalar Gain]',
#             list[3]:'[T-Squared Gain]',
#             list[4]:'[Trace Balance]',
#             list[5]:'[AGC]',
#             list[6]:'[Linear Gain]',
#             list[7]:'[Scalar Gain]',
#             list[8]:'[T-Squared Gain]',
#             list[9]:'[Trace Balance]'
#             }
#     return dict    

def const_dataEnhancementGroupAlgorithm():
    return [const_algBandpassPoststack(),
            const_algDilateErodeFilterPoststack(),
            const_algDirectionalSmoothPoststackVolume(),
            const_algFaultScannerPoststackVolume(),
            const_algGaussionFilterPoststackVolume(),
            const_algPhaseShiftPoststack(),
            const_algQuadratureTracePoststack(),
            const_algSlopesPoststackVolume(),
            const_algThinFaultLikelyHoodsPoststack(),
            
            const_algDecimatePoststack(),
            const_algVerticalSmoothPoststack(),
            "NEW - Stack Poststack Volume",
            const_algTrimStaticsPrestack(),
            #const_algInterpolatePrestack(),
            const_algBandpassPrestack(),
            const_algMutePrestack(),
            const_algPeakPickPoststack(),
            const_algPhaseShiftPrestack(),
            const_algQuadratureTracePrestack(),
            const_algStackPoststack(),
            const_algSupergatherPrestack(),
            const_algTrimStaticsPrestack(),
            const_algAngleMutePrestackVolume()
        ]     

# def const_dictDataEnhancementGroupAlgorithm():
#     list = const_dataEnhancementGroupAlgorithm()
#     dict = {
#             list[0]:'[Decimate]',
#             list[1]:'[Mute]',
#             list[2]:'[NEW - Stack]',
#             list[3]:'[Peak Pick]',
#             list[4]:'[Stack]',
#             list[5]:'[Supergather]',
#             list[6]:'[Trim Statics]'
#             }
#     return dict    

def const_SpectralDecompositionGroupAlgorithm():
    return [
            const_algPoststackCLSSAPrestack()
           ]

def const_dictClssaGroupAlgorithm(): #prestack
    list = const_clssaGroupAlgorithm()
    dict = {
            "CLSSA Prestack Volume":'[CLSSA]',
            }
    return dict

def const_velocityToolBoxGroupAlgorithm():
    return [  const_algCreateVelocityFieldPoststack(),

              const_algSemblancePrestack(),
              const_VelocityVolumeFromVerticalFunction(),
            "Create Velocity Field Poststack Volume",
            const_algNMOCorrectionPrestack(),
            "DerivePrestackObjectHwTimeVariantNMOFilterPluginTwoInputsInputsFlipped",
            const_algVelocityScalarPrestack(),
            "Velocity Scalar Prestack Volume",
            "W - NMO Prestack Volume",
            const_algVelocityConversionsInTimePoststack(),
            const_algDomainConverterPoststackHorizon(),
            const_algDomainConverterPrestack(),
            const_algDomainConverterPoststack()
            ]

# def const_dictVelocityToolBoxGroupAlgorithm():
#     list = const_velocityToolBoxGroupAlgorithm()
#     dict = {
#             list[0]:'[Velocity Conversions in time]',
#             list[1]:'[Velocity Conversions in depth]',
#             list[2]:'[Vertical Smooth]',
#             list[3]:'[Create Velocity Field]',
#             list[4]:'[Semblance]',
#             list[5]:'[Create Velocity Field]',
#             list[6]:'[NMO correction]',
#             list[5]:'[Velocity Scalar]',
#             list[6]:'[W - NMO Prestack]'
#             }
#     return dict
#     
def const_wideAzimuthGroupAlgorithm():
    return ["DerivePoststackObjectHWSteerFilterPlugin",
            "Steerable filter for several angles 4D Prestack Volume",
            "Directinal convolution Prestack Volume",
            const_algRadiusAndAzimuthPoststack2Horizons(),
            const_algOffsetAzimuthPrestack(),
            const_algOffsetAzimuthPrestackVolume(),
            const_algWideAzimuthCombine(),
            const_algRadiusandAzimuthPrestackVolume2Inputs(),
            const_algRadiusandAzimuthPoststackVolume2Inputs()
            ]
def const_forValidationGroupAlgorithm():
    return [
            const_algMathAttributeNEWPoststackHorizon(),
            const_algMath1AttributeNEWPoststack(),
            const_algSteerableFilterPoststack(),
            const_algSteerableFilter4DPrestack(),

            const_algDirectionalConvolutionPrestack(),
            const_algMath1AttributeNEWPrestack(),
            const_algNEWStackPoststack(),
            ]    

# def const_dictWideAzimuthGroupAlgorithm():
#     list = const_wideAzimuthGroupAlgorithm()
#     dict = {
#             list[0]:'[Steerable filter (oriented 2D convolution)]',
#             list[1]:'[Steerable filter for several angles 4D]',
#             list[2]:'[Directinal convolution]',
#             list[3]:'[Offset Azimuth Prestack Volume]'
#             }
#     return dict
#     
def const_AVOAnalysisAlgorithms():
    return [const_algOffsettoAnglePrestackVolume(),
            const_algOffsetToAnglePrestack2Inputs(),
            const_algAVOAttributesPoststack(),
            const_algAngleGatherPrestack(),
            const_algSTransformPoststack(),
            "NEW - Angle Gathers Prestack Volume"
            ]
    
def const_SQIAlgorithms():
    return [const_menuItemGatherTracker()]
    
# def const_dictAVOAnalysisAlgorithms():
#     list = const_AVOAnalysisAlgorithms()
#     dict = {
#             list[0]:'[Offset to Angle]',
#             list[1]:'[AVO Attributes]',
#             list[2]:'[Angle Gathers]',
#             list[3]:'[NEW - Angle Gathers]'
#             }
#     return dict

def const_domainConversionGroupAlgorithm():
    return ["Volume depth-to-time Prestack Volume",
            "DerivePrestackObjectHwTimeDepthConversionPluginTwoInputs",
            "Volume depth-to-time Poststack Volume",
            "Volume time-to-depth Poststack Volume",
            "Horizon depth-to-time Poststack Horizon",
            "Horizon time-to-depth Poststack Horizon",
#             "Seismic line time-to-depth",
#             "Seismic line depth-to-time",
            "Horizon time-to-depth Poststack Horizon",
            "Horizon depth-to-time Poststack Horizon",
            const_strCreateVelocityModel(),
            const_strCreateEditableVerticalFunctionSet(),
#             const_algVelocityConversionsInTimePoststack(),
            "Velocity Conversions in depth Poststack Volume",  
#             "Seismic line time-to-depth",
#             "Seismic line depth-to-time",
            const_algSeismicLineDepthToTime(),
            const_algSeismicLineTimeToDepth(),
            const_algSeismicLineTimeToDepthExtend(),
            const_algSeismicLineDepthToTimeExtend()
            ]
def const_domainConversionGroupAlgorithm2():
    return ["Seismic line time-to-depth",
            "Seismic line depth-to-time",
            ]
# def const_dictdomainConversionGroupAlgorithm():
#     list = const_domainConversionGroupAlgorithm()
#     dict = {
#             list[0]:'[Volume depth-to-time]',
#             list[1]:'[Volume time-to-depth]',
#             list[2]:'[Horizon depth-to-time]',
#             list[3]:'[Horizon time-to-depth]',
#             list[4]:'[Seismic line time-to-depth]',
#             list[5]:'[Seismic line depth-to-time]',
#             list[6]:'[Horizon time-to-depth]',
#             list[7]:'[Horizon depth-to-time]'
#             }
#     return dict        

def const_alphaStageGroupAlgorithm():
    return ["Pseudo azimuth gather Prestack Volume"]

def const_dictalphaStageGroupAlgorithm():
    list = const_alphaStageGroupAlgorithm()
    dict = {
            "Pseudo azimuth gather Prestack Volume":'[Pseudo azimuth gather]',
            }
    return dict

def const_attributesInstantaneousContextMenu():
    return "Attributes (Instantaneous)"

def const_attributesMultiTraceWindowedContextMenu():
    return "Attributes (Multi Trace Windowed)"

def const_attributeWindowedContextMenu():
    return "Attributes (Windowed)"

def const_clssaContextMenu():
    return "CLSSA"

def const_velocityToolBoxContextMenu():
    if conf_isRelease2018_1():
        return "Velocity Toolbox"    
    else: #for trunk
        return "Velocity toolbox"

def const_gainContextMenu():
    return "Gain"

def const_radonContextMenu():
    return "Radon"
############################################ ##############################################

##################################### Types of Headwave objects ###########################
##
###################################################################################
def const_typePhysicalContainerWidget():
    return "PhysicalContainerWidget"

def const_typePhysicalObjectCanvas():
    return "PhysicalObjectCanvasWidget"

def const_typeBoolPropertyWidget():
    return "BoolPropertyWidget"

def const_typeReferencePropertyWidget():
    if conf_isStaging():
        return "ReferencePropertyWidget"
    else:
        return "ObjectReferencePropertyWidget"
    
def const_typeCustomComboBoxWidget():
    return "CustomComboBoxWidget"
    
def const_typeCustomObjectBrowserLineWidget():
    return "CustomObjectBrowserLineWidget"

def const_typeCustomButtonWidget():
    return "CustomButtonWidget"

def const_typeCustomLineEditWidget():
    return "CustomLineEditWidget"

def const_typeObjectBrowserLinePlaceholderWidget():
    return "ObjectBrowserLinePlaceholderWidget"

def const_typeEnumPropertyWidget():
    return "EnumPropertyWidget"

def const_typeNumberPropertyWidget():
    return "NumberPropertyWidget"

def const_typeNumberx2PropertyWidget():
    return "Numberx2PropertyWidget"

def const_typeCustomTableHeadingWidget():
    return "CustomTableHeadingWidget"

def const_typeCustomButtonWidgetHeader():
    return "CustomButtonWidgetHeader"

def const_typeNumberx3PropertyWidget():
    return "Numberx3PropertyWidget"

def const_typeTextPropertyWidget():
    return "TextPropertyWidget"

def const_typeTextHeaderWidget():
    return "TextHeaderWidget"

def const_typeColorPropertyWidget():
    return "ColorPropertyWidget"

def const_typeObjectPlaceholderWidget():
    return "ObjectPlaceholderWidget"

def const_typeFilenamePropertyWidget():
    return "FilenamePropertyWidget"

def const_typeIndirectReferencePropertyWidget():
    if conf_isStaging():
        return "IndirectReferencePropertyWidget"
    else:
        return "IndirectObjectReferencePropertyWidget"
#NOTES: user-defined Type for the Inline/Crossline Columns in Input Tab of horizon
def const_typeNumberPair():
    return "NumberPair"

def const_typePairCombobox():
    return "EnumPropertyWidget"

def const_typeLabelCheckbox():
    return "LabelCheckbox"

def const_typeNumberx2AndNumber():
    return "Numberx2AndNumber"

def const_typeCustomTableHeadingWidget():
    return "CustomTableHeadingWidget"
########################################## Keys of Headwave objects ######################################################
# When HW objects could not be detected by real name but from nearby label, we apply key to get it

################### General Tab #########################
def const_keyMeasureCode():
    return "MeasureCode"

def const_keySampleRate():
    return "SampleRate"

def const_keySampleRateScale():
    return "SampleRateScale"

def const_keySampleRateCalculated():
    return "SampleRateCalculated"

def const_keySamples():
    return "Samples"

def const_keyAuthorityCode():
    return "AuthorityCode"

def const_keyReferenceCRS():
    return "ReferenceCRS"

def const_keyWKT():
    return "WKT"

def const_keyExportName():
    return "ExportName"

def const_keyDisplayName():
    return "DisplayName"

################### Input Tab #########################
def const_keySurveyReferenceVolume():
    return "SurveyReferenceVolume"

def const_keySourceShape():
    return "SourceShape"
                            
def const_keyHorizonTimeOption():
    return "HorizonTimeOption"

def const_keyXYUnitType():
    return "XYUnitType"

def const_keyExportHorizonObject(): 
    return "ExportHorizonObject"

def const_keyActiveAttributes():
    return "ActiveAttributes"

def const_keyExportShapeCRS():
    return "ExportShapeCRS"

def const_keyExportObject():
    return "ExportObject"

def const_keyExportPoststackObject():
    return "ExportPoststackObject"

def const_keyLinesToSkip():
    return "LinesToSkip"

def const_keyTimeDepthColumn():
    return "TimeDepthColumn"

def const_keyInlineCrosslineColumns():
    return "InlineCrosslineColumns"

def const_keyEastingNorthingColumns():
    return "EastingNorthingColumns"

def const_keyInlineColumn():
    return "InlineColumn"

def const_keyCrosslineColumn():
    return "CrosslineColumn"

def const_keyEastingColumn():
    return "EastingColumn"

def const_keyNorthingColumn():
    return "NorthingColumn"

def const_keyScaleFactorColumn():
    return "ScaleFactorColumn"

def const_keyFilePreview():
    return "FilePreview"

def const_keyInvalidValue():
    return "InvalidValue"

def const_keyPartialTemplateObject():
    return "PartialTemplateObject"

def const_keyLocalPosition():
    return "LocalPosition"

def const_keyLocalOrientationX():
    return "LocalOrientationX"

def const_keyLocalOrientationY():
    return "LocalOrientationY"

def const_keyLocalOrientationZ():
    return "LocalOrientationZ"

def const_keyLocalScale():
    return "LocalScale"
                        
def const_keyLocalPositionX():
    return "LocalPositionX"

def const_keyLocalPositionY(): 
    return "LocalPositionY"

def const_keyLocalPositionZ():
    return "LocalPositionZ"

def const_keyInputShapeObject():
    return "InputShapeObject"

def const_keyVASMode():
    return "VASMode"
def const_keyCloseSurface(): 
    return "IsCloseSurface"

## Stack/Prestack input
def const_keyInlineBytePosition():
    return "InlineBytePosition"

def const_keyCrosslineBytePosition():
    return "CrosslineBytePosition"

def const_keyEastingBytePosition():
    return "EastingBytePosition"

def const_keyNorthingBytePosition():
    return "NorthingBytePosition"

def const_keySEGYSortOrder():
    return "SEGYSortOrder"

def const_keyTimeDepth():
    return "keyTimeDepth"

def const_keyVelocitycolumn():
    return "keyVelocityColumn"

def const_keyFunctionType():
    return "keyFunctionType"
    
def const_keyActiveTrace():
    return "ActiveTrace"

def const_keyTraceValue():
    return "TraceValue"

def const_keyScaleBytePosition():
    return "ScaleBytePosition"

def const_keyScaleOverrideValue():
    return "ScaleOverrideValue"
## Used to click the checkbox only
def const_keyScaleOverrideValueLabel():
    return "ScaleOverrideValueLabel"

def const_keyCDPBytePosition():
    return "CDPBytePosition"

def const_keyFirstMinILMinXLPair():
    return "FirstMinILMinXLPair"

def const_keyFirstXYPair():
    return "FirstXYPair"

def const_keySecondMinILMaxXLPair():
    return "SecondMinILMaxXLPair"

def const_keySecondXYPair():
    return "SecondXYPair"

def const_keyThirdMaxILMaxXLPair():
    return "ThirdMaxILMaxXLPair"

def const_keyThirdXYPair():
    return "ThirdXYPair"

def const_keyDeadTraceBytePosition():
    return "DeadTraceBytePosition"

def const_keyDeadTraceSpecifierValue():
    return "DeadTraceSpecifierValue"

def const_keyUnit():
    return "Unit"

def const_keyZUnit():
    return "ZUnit"

def const_keyZUnitDropDown():
    return "ZUnitDropDown"

def const_keyXYUnit():
    return "XYUnit"

def const_keyAttribute():
    return "Attribute"

def const_keyOffset():
    return "Offset"

def const_keyReferenceID():
    return "ReferenceID"

def const_keyInvalidPropertyIssue():
    return "InvalidPropertyIssue"

def const_keyExportOption():
    return "Exportoption"

def const_keySurfaceUnit():
    return "SurfaceVerticalUnitOption"

def const_keySurfaceDepth():
    return "SurfaceVerticalDepthOption"

# def const_keyReferenceIDHorizon():
#     return "HorizonReferenceID"

# def const_keyLineToSkip():
#     return "LineToSkip"

def const_keyInline():
    return "Inline"

def const_keyCrossline():
    return "Crossline"

def const_keyEasting():
    return "Easting"

def const_keyNorthing():
    return "Northing"

def const_keyDepth():
    return "Depth"

def const_keySampleSize():
    return "SampleSize"

def const_keyInlineSize():
    return "InlineSize"

def const_keyCrosslineSize():
    return "CrosslineSize"

def const_keyInlineRange():
    return "InlineRange"

def const_keyOutputInlineRange():
    return "OutputInlineRange"

def const_keyOutputBinRange():
    return "OutputBinRange"
   
def const_keyOutputCrosslineRange():
    return "OutputCrosslineRange"

def const_keyOutputSampleRange():
    return "OutputSampleRange"

def const_keyOutputInlineRangeGoCAD():
    return "OutputInlineRangeGoCAD"

def const_keyOutputCrosslineRangeGoCAD():
    return "OutputCrosslineRangeGoCAD"

def const_keyOutputSampleRangeGoCAD():
    return "OutputSampleRangeGoCAD"

def const_keyUseHistogramValueRangeGoCAD():
    return "UseHistogramValueRangeGoCAD"
   
def const_keyCrosslineRange():
    return "CrosslineRange"

def const_keySampleRange():
    return "SampleRange"

def const_keyInlineStep():
    return "keyInlineStep"

def const_keyCrosslineStep():
    return "CrosslineStep"

def const_keySampleStep():
    return "SampleStep"

def const_keySampleCount():
    return "SampleCount"

def const_keyTraceRange():
    return "TraceRange"

def const_keyTraceStep():
    return "TraceStep"

def const_keyTraceCount():
    return "TraceCount"

def const_keyVMInlineStep():
    return "VMInlineStep"

def const_keyVMCrosslineStep():
    return "VMCrosslineStep"
   
def const_keyCrosslineSpacing(): 
    return "CrosslineSpacing"

def const_keyInlineSpacing(): 
    return "InlineSpacing"

def const_keyLatticeOrigin(): 
    return "LatticeOrigin"
                       
def const_keyCDPRange():
    return "CDPRange"

def const_keyCDPStep():
    return "CDPStep"

def const_keyCDPCount():
    return "CDPCount"

def const_keySampleUnit():
    return "SampleUnit"

def const_keyAttributeName():
    return "AttributeName"

def const_keyAttributeUnit():
    return "AttributeUnit"

def const_keyPetrelAddress():
    return "PetrelAddress"

def const_keyPetrelPort():
    return "PetrelPort"

def const_keyPetrelID():
    return "PetrelID"

def const_keyInputObject0():
    return "InputObject0"

def const_keyInputObject1():
    return "InputObject1"

def const_keyInputFiles():
    return "InputFiles"

##################### Behavior Tab #######################

def const_keyDisableCreationOfSurfaceAndPickObjects():
    return "DisableCreationSurfaceAndPickObjects"

def const_keyValueCriteria():
    return "ValueCriteria"

def const_keyReadonly():
    return "Readonly"

def const_keyTSClose():
    return "IsSurfaceClosed"

def const_keySetLatticeMethod():
    return "SetLatticeMethod"

def const_keyLatticeReference():
    return "LatticeReference"

def const_keyWorldOrigin():
    return "WorldOrigin"

def const_keyOrigin():
    return "Origin"

def const_keyWorldInlineSpacing():
    return "WorldInlineSpacing"

def const_keyWorldCrosslineSpacing():
    return "WorldCrosslineSpacing"
                    
def const_keyInlineRangeAndStep():
    return "InlineRangeAndStep"

def const_keyInlineRangeFrom():
    return "InlineRangeFrom"

def const_keyInlineRangeTo():
    return "InlineRangeTo"

def const_keyInlineCount():
    return "InlineCount"

def const_keyCrosslineRangeAndStep():
    return "CrosslineRangeAndStep"

def const_keyCrosslineRangeFrom():
    return "CrosslineRangeFrom"

def const_keyCrosslineRangeTo():
    return "CrosslineRangeTo"

def const_keyCrosslineCount():
    return "CrosslineCount"

def const_keyInlineInterval():
    return "InlineInterval"

def const_keyInlineAnnotationStep():
    return "InlineAnnotationStep"

def const_keyCrosslineAnnotationStep():
    return "CrosslineAnnotationStep"

def const_keyCrosslineInterval():
    return "CrosslineInterval"

def const_keyCornerPoint0():
    return "CornerPoint0"

def const_keyCornerPoint1():
    return "CornerPoint1"

def const_keyCornerPoint2():
    return "CornerPoint2"

def const_keyCrosslineLength():
    return "CrosslineLength"

def const_keyInlineLength():
    return "InlineLength"

def const_keyCrosslineOrientation():
    return "CrosslineOrientation"

def const_keyInlineOrientation():
    return "InlineOrientation"

def const_keyWorldCrosslineStep():
    return "WorldCrosslineStep"

def const_keyWorldInlineStep():
    return "WorldInlineStep"

def const_keyAnnotationOrigin():
    return "AnnotationOrigin"

def const_keyWhenExportComplete():
    return "WhenExportComplete"

def const_keyStart(): #For Petrel export
    return "Start"
def const_keyExportIsNotRunning(): #For Petrel export
    return "ExportIsNotRunning"

def const_keyExportIsRunning():
    return "ExportIsRunning"

def const_keyInlineLocation():
    return "Inlinelocation"

def const_keyCrosslineLocation():
    return "Crosslinelocation"

def const_keyTraceLocation():
    return "Tracelocation"

def const_keySampleLocation():
    return "SampleLocation"

def const_keyLineLocation():
    return "LineLocation"

def const_keyStepDistance():
    return "StepDistance"

def const_keyExportOptionColorTable():
    return "ExportOptionColorTable"

def const_keyAlphaScaleExportOptionColorTable():
    return "AlphaScaleExportOptionColorTable"

def const_keyAlphaScalerColorTable():
    return "AlphaScalerColorTable"

def const_keyOverallAlphaScale():
    return "OverallAlphaScale"

def const_keyTargetValueDimension():
    return "TargetValueDimension"

def const_keyClosed():
    return "IsSurfaceClosed"   

def const_keySegmentsA():
    return "SegmentA"
                        
def const_keySegmentsB():
    return "SegmentB"
                        
def const_keyAbsoluteVerticalRange():
    return "AbsoluteVerticalRange"

def const_keyRelativeVerticalRange():
    return "RelativeVerticalRange"

def const_keyGeologicAge():
    return "GeologicAge"

def const_keyActiveHorizonType():
    return "ActiveHorizonType"

def const_keyCorrespondingGeobodySurface():
    return "CorrespondingGeobodySurface"

def const_keyGeobodyGroup():
    return "GeobodyGroup"

def const_keyReferenceObject():
    return "ReferenceObject"

def const_keyAlternateReferencePosition():
    return "AlternateReferencePosition"

def const_keyReferencePosition():
    return "ReferencePosition"

def const_keySliceBefore():
    return "SliceBefore"

def const_keySliceAfter():
    return "SliceAfter"

def const_keyOffsetStep():
    return "OffsetStep"

def const_keyAlternateOffsetStep():
    return "Offset1"

def const_keyAlternateDirection():
    return "AlternateDirection"

def const_keySortOrder():
    return "SortOrder"

####################### Parameter Tab ##############
def const_keyOperation():
    return "Operation"

def const_keyMathOperation():
    return "MathOperation"

def const_keyButtonOperation():
    return "operationenumValue"

def const_keyMathConstantValue():
    return "MathConstantValue"

def const_keyAzimuthRangeValue():
    return "AzimuthRangeValue"

def const_keyTraceNumberRangeValue(): 
    return "TraceNumberRange"

def const_keyInlineSlicesFastAccess():
    return "InlineSlicesFastAccess"

def const_keyCrosslineSlicesFastAccess():
    return "CrosslineSlicesFastAccess"

def const_keySampleSlicesFastAccess():
    return "SampleSlicesFastAccess"

def const_keyVolumeFastAccess():
    return "VolumeFastAccess"

def const_keyOffsetRange():
    return "OffsetRangeValue"

def const_keyOutputTraceCount():
    return "OutputTraceCountValue"
def const_keyInputVelocityType():
    return "InputVelocitytype"

def const_keyOutputVelocityType():
    return "OutputVelocitytype"
## CSM
def const_keyVelocityPicks():
    return "VelocityPicks"

def const_keyVelocityScaleFunction():
    return "VelocityScaleFunction"

def const_keyReplacementVelocity():
    return "ReplacementVelocity"
    
def const_keyReferenceSurface():
    return "ReferenceSurface"

def const_keyReplacementVelocityMap():
    return "ReplacementVelocityMap"

def const_keyReplacementTimeDepthMap():
    return "ReplacementTimeDepthMap"

def const_keyVelocityAboveReferenceSurface():
    return "VelocityAboveReferenceSurface"

def const_keyConstantReplacementVelocity():
    return "ConstantReplacementVelocity"

def const_keyFirstSliceOffset():
    return "FirstSliceOffset"

def const_keySliceCount():
    return "SliceCount"

def const_keySliceInterval():
    return "SliceInterval"

def const_keyLastSliceOffset():
    return "LastSliceOffset"

def const_keyOutputAttribute():
    return "OutputAttribute"

def const_keyCorrectionMethod():
    return "CorrectionMethod"

def const_keyResetVisiblePerimeter():
    return  "ResetVisiblePerimeter"

def const_keyApplyVisiblePerimeter():
    return "ApplyVisiblePerimeter"

def const_keyResetCornerPointPerimeter():
    return "ResetCornerPointPerimeter"

def const_keyApplyCornerPointPerimeter():
    return "ApplyCornerPointPerimeter"

def const_keyDepthValueRange():
    return "DepthValueRange"

def const_keyVelocityValueRange():
    return "VelocityValueRange"

def const_keyTimeValueRange():
    return "TimeValueRange"

def const_keyMisteValueRange(): 
    return "MistieValueRange"

def const_keySeismicReferenceDatumMode(): 
    return "SeismicReferenceDatumMode"

def const_keyConstantEvaluation():
    return "SeismicReferenceDatumConstant"

def const_keyEvaluationMap(): 
    return "SeismicReferenceDatum"

def const_keySmoothingLength():
    return "SmoothingLength"

def const_keySmoothingRadius():
    return "SmoothingRadius"

def const_keyCopyInputDatumGriddingAndPerimeter():
    return "CopyInputDatumGriddingAndPerimeter"
    
def const_keyVerticalMax():
    return "VerticalMax"

def const_keyVintMax():
    return "VintMax"

def const_keyVelocityMax():
    return "VelocityMax"

def const_keyIncrement():
    return "Increment"

def const_keyExtendType():
    return "ExtendType"

def const_keyExtendVerticalFunctions():
    return "ExtendVerticalFunctions"

def const_keyPointSize():
    return "PointSize"

def const_keyXYUnitGoCAD():
    return "XYUnitGoCAD"

def const_keyUVWOrderGoCAD():
    return "UVWOrderGoCAD"

def const_keyAxisNU():
    return "AxisNU"

def const_keyAxisNV():
    return "AxisNU"

def const_keyAxisNW():
    return "AxisNU"

def const_keyPropertyUnit():
    return "PropertyUnit"

def const_keyVelocityUnit():
    return "VelocityUnit"

def const_keyMultipleIntersectionPolicy():
    return "MultipleIntersectionPolicy"

def const_keyLateralRangeMode():
    return "LateralRangeMode"

def const_keySpecifiedIntersection(): 
    return "SpecifiedIntersection"

def const_keyMergeMethod():
    return "MergeMethod"

def const_keyMergeOrder():
    return "MergeOrder"

def const_keyOverrideGridding():
    return "OverrideGridding"

def const_keyResamplePerTraceChannels():
    return "ResamplePerTraceChannels"

def const_keyForceAnnotationCoordinates():
    return "ForceAnnotationCoordinates"

def const_keyInlineStride():
    return "InlineStride"

def const_keyCrosslineStride():
    return "CrosslineStride"

def const_keyTransposeLineAnnotations():
    return "TransposeLineAnnotations"

####################### Geometry Tab ####################
def const_keyVertexCount():
    return "VertexCount"

def const_keyTriangleCount():
    return "TriangleCount"

def const_keyVertices():
    return "Vertices"

####################### Output Tab ####################
def const_keyOverallCompleteFactor():
    return "OverallCompleteFactor"

def const_keyHistogramScanning():
    return "HistogramCompleteFactor"

def const_keyDatasetCompeleteFactor():
    return "DatasetCompleteFactor"
        
def const_keyVelocityModel():
    return "VelocityModel"

def const_keyValueSpace():
    return "ValueSpace"

def const_keyAttributeDimension():
    return "AttributeDimension"

def const_keyAttributeUnit():
    return "AttributeUnit"

def const_keyOverallCompleteFactor2DStack():
    return "OverallCompleteFactor2DStack"

def const_keyOverallCompleteFactor2DGather():
    return "OverallCompleteFactor2DGather"

def const_keyOverallCompleteFactor3DStack():
    return "OverallCompleteFactor3DStack"

def const_keyOverallCompleteFactor3DPrestack():
    return "OverallCompleteFactor3DPrestack"

def const_keyOverallCompleteFactorSEGYExporter():
    return "OverallCompleteFactorSEGYExporter"

def const_keyUnitOverallCompleteFactor():
    return "UnitOverallCompleteFactor"

def const_keyUnitOverallCompleteFactor2DStack():
    return "UnitOverallCompleteFactor2DStack"

def const_keyUserSpecifiedCachefileName():
    return "UserSpecifiedCachefileName"

def const_keyOverallCachingStatus():
    return "OverallCachingStatus"

def const_keyRealizeStatus():
    return "DatasetCompleteStatus"

def const_keyReferenceShape():
    return "ReferenceShape"

def const_keyCacheFileName():
    return "CacheFileName"

def const_keyCacheToDisk():
    return "CacheToDisk"

def const_keyCacheToDisk2DStack():
    return "CacheToDisk2DStack"

def const_keyBrowseExport():
    return "BrowseExport"

def const_keyBrowseCache():
    return "BrowseCache"
    
def const_keyBrowseCacheSEGYExporter():
    return "BrowseCacheSEGYExporter"

def const_keyStartExport():
    return "StartExport"

def const_keyStopExport() : 
    return "StopExport"

def const_keyCompressionMethod():
    return "CompressionMethod"

def const_keyCompressionMethodRelease2018():
    return "CompressionMethodRelease2018"

def const_keyCompressionPreviewMethod():
    return "CompressionPreviewMode" 

def const_keyCompressionTolerance():
    return "CompressionTolerance"

def const_keyDataSize():
    return "DataSize"

def const_keyValueRange():
    return "ValueRange"

def const_keyEstimatedValueRange():
    return "EstimatedValueRange"

def const_keyValueRangeFrom():
    return "ValueRangeFrom"

def const_keyValueRangeTo():
    return "ValueRangeTo"

def const_keyEastingRange():
    return "EastingRange"

def const_keyEastingRangeFrom():
    return "EastingRangeFrom"

def const_keyEastingRangeTo():
    return "EastingRangeTo"

def const_keyNorthingRange():
    return "NorthingRange"

def const_keyNorthingRangeFrom():
    return "NorthingRangeFrom"

def const_keyNorthingRangeTo():
    return "NorthingRangeTo"

def const_keyStartZ():
    return "StartZ"

def const_keyInlineDecimation():
    return "InlineDecimation"

def const_keyCrosslineDecimation():
    return "CrosslineDecimation"

def const_keyTimeDepthRange():
    return "TimeDepthRange"
## Ouput tab of stack/prestack
def const_keyHistogramTracesToRead():
    return "HistogramTracesToRead"

def const_keyHistogramAutoscanEnabled():
    return "HistogramAutoscanEnabled"

def const_keyAnalyzerStatus():
    return "AnalyzerStatus"

def const_keyPetrelInlineRange():
    return "PTInlineRange"

def const_keyPetrelCrosslineRange():
    return "PTCrosslineRange"

def const_keyPetrelTimeRange():
    return "PTTimeRange"

def const_keyPetrelInputInlineStep():
    return "PTInputInlineStep"

def const_keyPetrelInputCrosslineStep():
    return "PTInputCrosslineStep"

def const_keyPetrelInputTimeStep():
    return "PTInputTimeStep"

def const_keyPetrelInputInlineRange():
    return "PTInputInlineRange"

def const_keyPetrelInputCrosslineRange():
    return "PTInputCrosslineRange"

def const_keyPetrelInputTimeRange():
    return "PTInputTimeRange"

def const_keyOffsetRangeLogical():
    return "OffsetRangeLogical"

def const_keyOffsetSpacingLogical():
    return "OffsetSpacingLogical"

def const_keyOffsetRangePhysical():
    return "OffsetRangePhysical"

def const_keyOffsetSpacingPhysical():
    return "OffsetSpacingPhysical"

def const_keySampleRangePhysical():
    return "SampleRangePhysical"

def const_keySampleStepPhysical():
    return "SampleStepPhysical"

def const_keyExporterXYUnit():
    return "ExporterXYUnit"

def const_keyExporterAttributeUnit():
    return "ExporterAttributeUnit"

####################### Visualization Tab ##############
def const_keyEnableVisualization():
    return "EnableVisualization"

def const_keyRemoveTwoWayBlending():
    return "RemoveTwoWayBlending"

def const_keyRemoveThreeWayBlending():
    return "RemoveThreeWayBlending"

def const_keyIntersectionRenderingEnabled():
    return "IntersectionRenderingEnabled"

def const_keyVizScope3DWindow():
    return "VolumeObject3DOrWindowScope"

def const_keyVizScopeHorizonWindow():
    return "HorizonTypeObjectOrWindowScope"

def const_keyVizScopeVolumeSliceWindow():
    return "VolumeSliceOrWindowScope"

def const_keyVizScopeLineWindow():
    return "LineModelOrWindowScope"

def const_keyVizScopePointsetWindow():
    return "PointSetOrWindowScope"

def const_keyVizScopeSurfaceWindow():
    return "SurfaceModelOrWindowScope"

def const_keyLineWeight():
    return "Lineweight"

def const_keyAttributes():
    return "Attributes"

def const_keyBlendingMode():
    return "Blendingmode"

def const_keyAttribute1():
    return "Attribute1"

def const_keyAttribute2():
    return "Attribute2"

def const_keyAttribute3():
    return "Attribute3"

def const_keyColorTable1():
    return "ColorTable1"

def const_keyColorTable3D():
    return "ActiveTransferFunction3D"

def const_keyOverrideValueRange():
    return "OverrideValueRange"

def const_keyColor():
    return "Color"

def const_keyCRS():
    return "CRS"

def const_keyDisplayContours():
    return "DisplayContours"

def const_keyDisplayContourLinesEvery():
    return "DisplayContourLinesEvery"

def const_keyDisplayContourLinesBetween():
    return "DisplayContourLinesBetween"

def const_keyDisplayContourRangeFrom():
    return "DisplayContourRangeFrom"

def const_keyDisplayContourRangeTo():
    return "DisplayContourRangeTo"

def const_keyDisplayContourAnnotations():
#     return "DisplayContourAnnotations"
    return "ContourAnnotationSize"

def const_keyEnableBoundingBox():
    return "EnableBoundingBox"

def const_keyReadoutMethod():
    return "ReadoutMethod"

def const_keyHorizonVisualizationMode():
    return "HorizonVisualizationMode"

def const_keyConstrainingHorizon():
    return "ConstrainingHorizon"

def const_keyTargetPoststack():
    return "TargetPoststack"

def const_keyTargetVolumeTransferFunction():
    return "TargetVolumeTransferFunction"

def const_keyThicknessStart():
    return "ThicknessStart"

def const_keyThicknessStop():
    return "ThicknessStop"

def const_keyMinimumTime():
    return "MinimumTime"
def const_keyMinimumTime2D():
    return "MinimumTime2D"

def const_keyMinimumDepth2D():
    return "MinimumDepth2D"

def const_keyMaximumTime():
    return "MaximumTime"

def const_keyMaximumTime2D():
    return "MaximumTime2D"

def const_keyMaximumDepth2D():
    return "MaximumDepth2D"

def const_keyTimeIncrement():
    return "TimeIncrement"

def const_keyTimeIncrement2D():
    return "TimeIncrement2D"

def const_keyDepthIncrement2D():
    return "DepthIncrement2D"

def const_keyInterpolation():
    return "Interpolation"

def const_keyMinimumDepthInMeter():
    return "Minimum_depth_in_meter"

def const_keyMaximumDepthInMeter():
    return "Maximum_depth_in_meter"

def const_keyDepthIncrementInMeter():
    return "Depth_increment_in_meter"

def const_keyInclusionDataRange():
    return "InclusionDataRange"

def const_keyTaperLength():
    return "TaperLength"

def const_keyNumberOfPairs():
    return "NumberOfPairs"

def const_keyTimet1():
    return "Time t1"

def const_keyTimet2():
    return "Time t2"

def const_keyTimet3():
    return "Time t3"

def const_keyTimet4():
    return "Time t4"

def const_keyTimet5():
    return "Time t5"

def const_keyTimet6():
    return "Time t6"

def const_keyTimet7():
    return "Time t7"

def const_keyTimet8():
    return "Time t8"

def const_keyMute1():
    return "Mute 1"

def const_keyMute2():
    return "Mute 2"

def const_keyMute3():
    return "Mute 3"

def const_keyMute4():
    return "Mute 4"

def const_keyMute5():
    return "Mute 5"

def const_keyMute6():
    return "Mute 6"

def const_keyMute7():
    return "Mute 7"

def const_keyMute8():
    return "Mute 8"

def const_keyAutoEnableMute():
    return "AutoEnableMute"

def const_keyOffsetScale():
    return "OffsetScale"

def const_keyValueCutoff():
    return "ValueCutoff"

def const_layoutSchemeValue():
    return ["Extra large", "Large", "Small", "Extra small", "Medium"]

def const_displaySettingValue():
    return ["Compact", "Full", "Relative"]

def const_buildIncolorTable1D():
    return ["Rainbow", "Blue/Red", "Greyscale", "Geobody", "Heat", "Voxet", "Velocity", "Head (inverse)"]

def const_getAlgNameFromDeriveCombine(strAlgName):    
    dictAlgName = {'Alice': '2341',
                   'Beth': '9102',
                   'Cecil': '3258',
                  }

def const_keyOutputTypeParOfPeakPickAlg():
    return "IntParameterObjectOutputtype"    

def const_keyNMOOperation():
    return "NMOOperation"

def const_keyDefaultSurfaceRenderingMode(): 
    return "DefaultSurfaceRenderingMode"
 
########################     Well    ############################
def const_menuWellExplorer():
    return "NewExplorerWindow1"

def const_menuWellHeadsExplorer():
    return "NewExplorerWindow."

def const_keyNameColumn():
    return "NameColumn"

def const_keyKellyBushingColumn():
    return "KellyBushingColumn"

def const_keyTotalMDColumn():
    return "TotalMDColumn"

def const_keyDepthUnit():
    return "DepthUnit"

def const_keyTimeUnit():
    return "TimeUnit"

def const_keyNegateDepthValues():
    return "NegateDepthValues"

def const_keyDepthColumn():
    return "DepthColumn"

def const_keyTimeColumn():
    return "TimeColumn"

def const_keyTargetWell():
    return "Target well"

def const_keyWellNameColumn():
    return "Well name column"

def const_keyMarkerNameColumn():
    return "Marker name column"

def const_keyKBDepthDatum():
    return "DefaultDepthDatumToKellyBushing"

def const_keyMDColumn():
    return "MD column"

def const_keyColumnBreaks():
    return "Column Breaks"

def const_keyMDButton():
    return "MDButton"

def const_keyTWTButton():
    return "TWTButton"

def const_keyCreateTWT():
    return "CreateTWT"

def const_keyCreateDepth():
    return "CreateDepth"

def const_keyXButton():
    return "XButton"

def const_keyYButton():
    return "YButton"

def const_keyTVDKBButton():
    return "TVDKBButton"

def const_keyTVDSSButton():
    return "TVDSSButton"

def const_keyCreateFullySpecifiedControlPoint():
    return "CreateFullySpecifiedControlPoint"

def const_keyAzimuthHistogramTable():
    return "AzimuthHistogramTable"

def const_keyVerticalDistanceUnit():
    return "VerticalDistanceUnit"

def const_keyDxColumn():
    return "DxColumn"

def const_keyDyColumn():
    return "DyColumn"

def const_keyTVDSSColumn():
    return "TVDSSColumn"

def const_keyTVDKBColumn():
    return "TVDKBColumn"

def const_keyAzimuthColumn():
    return "AzimuthColumn"

def const_keyInclinationColumn():
    return "InclinationColumn"

def const_keyDepthColumnType():
    return "DepthColumnType"

def const_keyTargetWellObject():
    return "TargetWellObject"

def const_keyKellyBushing():
    return "KellyBushing"

def const_keyLocationX():
    return "LocationX"

def const_keyLocationY():
    return "LocationY"

def const_keyUWI():
    return "UWI"

def const_keyMistieValue():
    return "MistieValue"

def const_keyOwningWell():
    return "OwningWell"

def const_keyActivePath():
    return "ActivePath"
def const_keyActiveCheckshot():
    return "ActiveCheckshot"

def const_keyMeasuredDepth():
    return "MeasuredDepth"

def const_keyStopMeasuredDepth():
    return "StopMeasuredDepth"

def const_keyStartMeasuredDepth():
    return "StartMeasuredDepth"

def const_keyThickness():
    return "Thickness"

def const_keyRadius():
    return "Radius"

def const_keyMarkerRadius():
    return "MarkerRadius"

def const_keyLogRadius():
    return "LogRadius"

def const_keyDisplayColor():
    return "DisplayColor"

def const_keyDefaultShowLocation():
    return "DefaultShowLocation"

# Data tab of Well - DO NOT CHANGE THE CONTENT
def const_keyMDTable():
    return "MD*Table"

def const_keyTwtTable():
    return "Twt*Table"

def const_keyTwtTableDatumed():
    return "TwtTableDatumed"

def const_keyTvdssTable():
    return "TvdssTable"

def const_keyTvdssTableDatumed():
    return "TvdssTableDatumed"

def const_keyVrmsTable():
    return "VrmsTable"

def const_keyVrmsBelowDatumTable():
    return "VrmsBelowDatumTable"

def const_keyVavgTable():
    return "VavgTable"

def const_keyVavgBelowDatumTable():
    return "VavgBelowDatumTable"

def const_keyVintTable():
    return "VintTable"

def const_keyDisplayModeWellPath():
    return "ActiveWellPathDisplayMode"

def const_keyDisplayModeWellLog():
    return "ActiveWellLogDisplayMode"

def const_keyLogTable():
    return "LogTable"

# def const_CreateTWTUnit():
#     return "CreateTWTUnit"
#
# def const_CreateDepthUnit():
#     return "CreateDepthUnit"
######################## Petrel Only ############################
def const_keyOriginX():
    return "OriginX"

def const_keyOriginY():
    return "OriginY"

def const_keyEndFirstILX():
    return "EndFirstILX"

def const_keyEndFirstILY():
    return "EndFirstILY"

def const_keyEndFirstXLX():
    return "EndFirstXLX"

def const_keyEndFirstXLY():
    return "EndFirstXLY"

def const_keySeismicTemplate():
    return "SeismicTemplate"

def const_keyVelocityTemplate():
    return "VelocityTemplate"

def const_keyViewAll():
    return "ViewAll"

def const_keyYes():
    return "Yes"

def const_keyNo():
    return "No"

def const_keyOpen():
    return "Open"

def const_keyOK():
    return "OK"

def const_keyExit():
    return "Exit"

def const_keyLineDown():
    return "LineDown"

def const_keyLineUp():
    return "LineUp"

def const_keyContinueSpatiallyUnaware():
    return "ContinueSpatiallyUnaware"

def const_keyImportFile():
    return "ImportFile"

def const_keyFilename():
    return "Filename"

def const_keyColorOther():
    return "ColorOther"

def const_keyColorRed():
    return "ColorRed"

def const_keyColorGreen():
    return "ColorGreen"

def const_keyColorBlue():
    return "ColorBlue"

def const_keyAddColorToCustom():
    return "AddColorToCustom"

def const_keySelect():
    return "Select"

def const_keyCopy():
    return "Copy"

def const_keyPaste():
    return "Paste"

def const_typeListItem():
    return "ListItem"

def const_typeButton():
    return "Button"

def const_typeDataItem():
    return "DataItem"

def const_typeEdit():
    return "Edit"

def const_objectTypeSeismic():
    return "Seismic"

def const_objectTypeVelocity():
    return "Velocity"

def const_objectTypeHorizon():
    return "Horizon"

def const_objectTypeSurface():
    return "Surface"

def const_objectTypeHorizonPickedFromPetrel():
    return "HorizonPick"
def const_objectTypeExportedHorizon():
    return "ExportedHorizon"

def const_objectType2DSeismic():
    return "2DSeismic"

def const_keyMin():
    return "Min"

def const_keyMax():
    return "Max"

def const_keyNoOfSamplePerTrace():
    return "NoOfSamplePerTrace"

def const_keyNoOfTrace():
    return "NoOfTrace"

def const_keyNoOfTriangles():
    return "NoOfTriangles"

def const_keyNoOfVertices():
    return "NoOfVertices"

def const_keyAzimuth():
    return "Azimuth"

def const_keyAzimuthReadoutPolicy():
    return "AzimuthReadoutPolicy"

def const_keyTypeOfSurface():
    return "TypeOfSurface"

def const_keyOriginalIncX():
    return "OriginalIncX"

def const_keyOriginalIncY():
    return "OriginalIncY"

def const_keyOriginalMinX():
    return "OriginalMinX"

def const_keyOriginalMaxX():
    return "OriginalMaxX"

def const_keyOriginalMinY():
    return "OriginalMinY"

def const_keyOriginalMaxY():
    return "OriginalMaxY"

def const_keySurfaceICount():
    return "SurfaceICount"

def const_keySurfaceJCount():
    return "SurfaceJCount"

def const_keySurveyAndPlansCount():
    return "SurveyAndPlans"

def const_keyInterpolateOverrideGriddingMode():
    return "OverrideGridding"

def const_keyAdjacentILGathers():
    return "AdjacentILGathers"

def const_keyAdjacentXLGathers():
    return "AdjacentXLGathers"

def const_keyStackSupergather():
    return "StackSupergather"
######################## View title ###########################
def const_viewXYTWT():
    return "X/Y/TWT"

def const_viewXYDepth():
    return "X/Y/Depth"

def const_viewXYZ():
    return "X/Y/Z"

def const_viewXY():
    return "X/Y"

def const_viewSectionTWT():
    return "Section/TWT"

def const_viewSectionDepth():
    return "Section/Depth"

def const_viewXYFrequency():
    return "X/Y/Frequency"

def const_viewCrossplot():
    return "Intercept/Gradient"

######################## View type ###########################
def const_viewTypeAll():
    return "View all"

def const_viewTypeFit(): # for section view
    return "View Fit"

def const_viewFromTopType():
    return "View from top"

def const_viewFromAboveType():
    return "View from above"

def const_viewFromBelowType():
    return "View from below"

def const_viewFromBottomType():
    return "View from bottom"

def const_viewFromEastType():
    return "View from east"

def const_viewFromWestType():
    return "View from west"

def const_viewFromNorthType():
    return "View from north"

def const_viewFromSouthType():
    return "View from south"

######################## string ###########################
def const_strInline():
    return "Inline"

def const_strCrossline():
    return "Crossline"

def const_strSlice():
    return "Slice"

def const_strGather():
    return "Gather"

def const_strGather2D():
    return "Gather2D"

def const_strInlineObject():
    return "InlineObject"

def const_strCrosslineObject():
    return "CrosslineObject"

def const_strHorizontalSliceObject():
    return "HorizontalSliceObject"

def const_strGatherSliceObject():
    return "GatherSliceObject"

def const_strGather2DSliceObject():
    return "Gathers2DSliceObject"

def const_strHorizonShape():
    return "HorizonShapeObject"

def const_strHorizonPick():
    return "HorizonPickObject"

def const_strHorizontalSlice():
    return "HorizontalSlice"

def const_strInlinePrestackVolume():
    return "InlinePrestackVolume"

def const_strCrosslinePrestackVolume():
    return "CrosslinePrestackVolume"

def const_strInlineContextMenu():
    return "Inline"

def const_strCrosslineContextMenu():
    #return "InstantiateCrosslineObject"
    return "Crossline"

def const_strPlaneContextMenu():
    return "InstantiateAlternateGatherSliceObject"

# def const_strHorizonAttributeFromPostStack():
#     return "HWHorizonAttributeFromPoststack"


#  New Poststack horizon attribute Explorer
def const_strNewPoststackHorizonAttributeExplore():
    return "NewExplorerWindow.1"

def const_strViewContextMenu():
    return "View.ChildMenu"

def const_strExtractVerticalFunctions():
    return "JoinedAttribute"
# Editable version
def const_strCreateEditableVerticalFunctionSet():
    #return "CreateEditableVerticalFunctionSet"
    return "Free-form velocity vertical function set"

# Velocity Model
def const_strCreateVelocityModel():
    return "CreateVelocityModel"

# Extract vertical functions': [JoinedAttribute

def const_strHorizontalSliceContextMenu():
    return "InstantiateHorizontal*SliceObject"
    #return "InstantiateHorizontalPrestackSliceObject"

def const_strGatherSliceContextMenu():
    return "InstantiateGatherSliceObject"

def const_strGather2DContextMenu():
    return "InstantiateGathers2DSliceObject"

def const_strCreateSubvolumeContextMenu():
    return "InstantiateProbe3DObject"

# Velocity volume from vertical function
def const_VelocityVolumeFromVerticalFunction():
    return "HWVolumeFromVerticalFunctionSetPlugin"

# Context menu
def const_StartPetrelExportObjectName():
    return "Start"

######################## Data file extension ###########################
def const_extensionFileALUT():
    return "alut"
def const_extensionFileSGY():
    return "sgy"

def const_extensionFileSEGY():
    return "segy"

def const_extensionFileVO():
    return "vo"

def const_extensionFileTXT():
    return "txt"

def const_extensionFileSMF():
    return "SMF"

def const_extensionFilePRN():
    return "prn"

def const_extensionFileCSV():
    return "csv"

def const_extensionFileLAS():
    return "las"

def const_extensionFileVOAA():
    return "voaa"

def const_extensionFileHOR():
    return "hor"

def const_extensionFileASCII():
    return "ascii"

def const_extensionFileVDS():
    return "vds"

def const_extensionFileASC():
    return "ASC"

def const_extensionFileTS():
    return "ts"

def const_SEGYStacked2DLineImportObject():
    return "SEGYStacked2DLineImportObject"

def const_SEGYGathers2DLineImportObject():
    return "SEGYGathers2DLineImportObject"

def const_SEGYPoststackImportObject():
    return "SEGYPoststackImportObject"

def const_SEGYPrestackImportObject():
    return "SEGYPrestackImportObject"

def const_SEGYExporter():
    return "SEGYExporter"

def const_GoCadExporter():
    return "GoCadExporter"

def const_WorkflowPoststackImporter():
    return "3D poststack SEGY"

def const_WorkflowPrestackImporter():
    return "3D prestack SEGY"

def const_ViewPoststackVolume():
    return "View poststack volume"

def const_SeismicContainer():
    return "SeismicContainer"

def const_Unassociated3DPoststack():
    return "Unassociated 3D poststack"

def const_UnassociatedPrestack():
    return "Unassociated 3D prestack"

#------------------- Sort order -----------------
def const_InlineSortOrder():
    return "Inlines"

def const_CrosslineSortOrder():
    return "Crosslines"
#------------------- System container -----------------
def const_WellDataContainerObjectName():
    return "{Misc:WellData}.ObjectPlaceholderWidget"

def const_WellContainerObjectName():
    return "{Object:WellContainer:DisplayName}.ObjectPlaceholderWidget"

def const_WellLogsContainerObjectName():
    return "Logs.ObjectPlaceholderWidget"

def const_WellPathsContainerObjectName():
    return "Paths.ObjectPlaceholderWidget"

def const_WellCheckshotsContainerObjectName():
    return "Checkshots.ObjectPlaceholderWidget"

def const_UnassociatedHorizonsObjectName():
    return "{Misc:UnassociatedHorizons}.ObjectPlaceholderWidget"

def const_VelocityPickEditorObjectName():
    return "Velocity Pick Editor.ObjectPlaceholderWidget"

def const_WorkflowContainerObjectName():
    return "{Object:WorkflowContainer:DisplayName}.ObjectPlaceholderWidget"

def const_RunningApplicationObjectName():
    return "Running Applications"
#------------------------------------------------------
def const_AttachToCheckshotsContextMenu():
    return "*attach*Checkshots*"

def const_HorizonPicksText():
    return "[Triangle surface] [Point Set]"

def const_HorizonShapeText():
    return "[Triangle surface]"

def const_VelocityModel():
    return "Velocity model"

def const_VerticalFunctions():
    return "Vertical functions"

def const_ActiveVerticalFunctions():
    return "Active vertical functions"

def const_TimeSliceModel():
    return "Time slice model"

def const_ModelBoundaries():
    return "Model boundaries"

def const_keyTvdkbTable():
    return "TvdkbTable"

def const_keyPtLogNumbers():
    return "Includes sub folders:"

def const_keyPtMarkerNumbers():
    return "Number of points in the filter:"

### User Preferences
def const_namingPolicy_OperationType():
    return "Operation type"

def const_namingPolicy_FullDescription():
    return "Full Description"

def const_namingPolicy_Datatype():
    return "Data type"

def const_InVA_VelocitySemblancePane():
    return "Velocity Semblance"

def const_InVA_EtaSemblancePane():
    return "Eta Semblance"

def const_InVA_ResidualSemblancePane():
    return "Residual Semblance"

def const_InVA_GatherPane():
    return "Gather"

def const_InVA_MiniStackPane():
    return "Mini-stack"

def const_InVA_StackPane():
    return "Stack"

def const_InVA_MapPane():
    return "Map"

def const_InVA_Title():
    return "Velocity Analysis"

def const_keyVelScanMin():
      return "VelScanMin"

def const_keyVelScanMax():
      return "VelScanMax"

def const_keyVelScanStep():
      return "VelScanStep"
 
def const_keyEtaExtent():
      return "EtaExtent"
  
def const_keyEtaIncrementValue():
    return "EtaIncrementValue"
  
def const_keyVelocityScaleFactor():
      return "VelocityScaleFactor"
  
def const_keyVelocityPercentagesRange():
      return "VelocityPercentagesRange"
  
def const_keyVelocityPercentagesStep():
      return "VelocityPercentagesStep"
  
def const_keyStackTraceRange():
      return "StackTraceRange"
  
def const_keyVelocityExtent():
      return "VelocityExtent"
  
def const_keyVelocityStep():
      return "VelocityStep"
  
def const_keyAdjacentTraces():
      return "AdjacentTraces"
  
def const_keyAdjacentTraceOption():
      return "AdjacentTraceOption"
  
def const_keyPrestackILXLIntervals():
      return "PrestackILXLIntervals"
  
def const_keyPrestackILXLLengths():
      return "PrestackILXLLengths"
  
def const_keyRoundILIntervals():
      return "RoundILIntervals"
  
def const_keyRoundXLIntervals():
      return "RoundXLIntervals"
  
def const_keyEffectiveILIntervals():
      return "EffectiveILIntervals"
  
def const_keyEffectiveXLIntervals():
      return "EffectiveXLIntervals"
  
def const_keyInfiniteVoxel():
    return "InfiniteVoxelResolution"

def const_keyVFSetILXLLength():
    return "VFSetILXLLength"
  
def const_keyInputVF_InVA():
      return "InputVF_InVA"
  
def const_keyInputGathers_InVA():
      return "InputGathers_InVA"
  
def const_keyViz_InVA():
      return "Viz_InVA"
  
def const_keyILLocation_InVA():
      return "ILLocation_InVA"
  
def const_keyXLLocation_InVA():
      return "XLLocation_InVA"
  
def const_keyOverrideSectionViewRange_InVA():
      return "OverrideSectionViewRange_InVA"
 
def const_tabAlgoParam():
     return "tabAlgoParam"
 
def const_tabLatticeInVA():
    return "tabLattice"
 
def const_tabMapInVA():
     return "tabMap"
 
def const_tabPoststackHorizons():
    return "tabPoststackHorizons"
 
def const_inputVizParams():
     return "inputVizParams"
 
 #Prestack autotracking
def const_keyPrimaryTrackingMethod():
    return "PrimaryTrackingMethod"

def const_keyAutotrackAlongGather():
    return "AutotrackAlongGather" 

def const_keyFlatnessCutoff():
    return "FlatnessCutoff" 
 
def const_zoneModel():
     return "Zone model"

def const_zoneIDVolume():
     return "Zone ID volume"
 
def const_createLinkedSliceGroup():
    return "createLinkedConstrainedVolumeObjectContainer"

def const_ungroupLinkedSliceGroup():
    return "liquidateLinkedConstrainedVolumeObjectContainer"

def const_algDeriveHorizonTriangleSurface():
    return "DeriveHorizonTriangleSurface"

def const_algDeriveHorizonPointSurface():
    return "DeriveHorizonPointSurface"

def const_Merge3DPrestackImportButton():
    return com_strFileImportType("prestack volume from SEGY file(s) [Merge]")

def const_2DGathersImportButton():
    return com_strFileImportType("Gathers 2D-line from SEGY file(s)")

def const_2DStackImportButton():
    return com_strFileImportType("Stacked 2D-line from SEGY file(s)")

def const_3DPoststackImportButton():
    return com_strFileImportType("3D poststack volume from SEGY file(s)")

def const_3DPrestackImportButton():
    return com_strFileImportType("3D prestack volume from SEGY file(s)")

def const_3DVerticalFunctionsImportButton():
    return com_strFileImportType("3D vertical functions")

def const_3DGoCADImportButton():
    return com_strFileImportType("3D volume from GoCAD voxet file (.vo)")

def const_ConvertedDataImportButton():
    return com_strFileImportType("Load converted data set")

def const_WellPathClosestNameMatchingImportButton():
    return com_strFileImportType("Deviation well path (closest name matching)")

def const_WellPathExactNameMatchingImportButton():
    return com_strFileImportType("Deviation well path (exact name matching)")

def const_WellPathNoNameMatchingImportButton():
    return com_strFileImportType("Deviation well path (no name matching)")

def const_WellPathUWIMatchingImportButton():
    return com_strFileImportType("Deviation well path (UWI matching)")

def const_ASCIIHorizonImportButton():
    return com_strFileImportType("Horizon from ASCII file")

def const_WellCheckshotImportButton():
    return com_strFileImportType("Well checkshot")

def const_WellHeadImportButton():
    return com_strFileImportType("Well heads from ASCII file")

def const_WellLogClosestNameMatchingImportButton():
    return com_strFileImportType("Well log from LAS (closest name matching)")

def const_WellLogExactNameMatchingImportButton():
    return com_strFileImportType("Well log from LAS (exact name matching)")

def const_WellLogUWIMatchingImportButton():
    return com_strFileImportType("Well log from LAS (UWI matching)")

def const_WellMarkerClosestNameMatchingImportButton():
    return com_strFileImportType("Well marker (closest name matching)")

def const_WellMarkerExactNameMatchingImportButton():
    return com_strFileImportType("Well marker (exact name matching)")

def const_WellMarkerUWIMatchingImportButton():
    return com_strFileImportType("Well marker (UWI matching)")

def const_PointsetImportButton():
    return com_strFileImportType("Point set: From .smf file")
    
def const_TriangulatedSurfaceImportButton():
    return com_strFileImportType("Triangulated surface: From .smf file")

def const_ScalingfunctionsImportButton():
    return com_strFileImportType("Scaling functions: From ASCII file")

def const_geometryGroup():
    return "Geometry"

def const_surfaceModelGroup():
    return "Surface models"

def const_triangleSurfaceGroup():
    return "Triangle surfaces"

def const_fileTriangleSurfaceContextMenu():
    return "File triangle surface"

def const_keyFillHolesHorizon():
    return "Fill holes"

def const_keyIsWorkflowActive():
    return "IsWorkflowActive"

def const_strWorkflowObjectName():
    return "Workflow."

def const_strAVOQCDisplayName():
    return "AVO QC"

def const_strAutotrackHorizonObject():
    return "Autotracker"

def const_strProjectObjName():
    return ".Project.DisplayName"

def const_strTriangleSetContainerObjName():
    return "TriangleSetContainer"

def const_keyDisplayObjectType():
    return "DisplayObjectType"

def const_keyVFControlPoints():
    return "VFControlPoints"

def const_keyWiggleCount():
    return "WiggleCount"

def const_keyWigglePlotType():
    return "WigglePlotType"

def const_ContainerCulture():
    return "Culture data"

def const_ContainerPoints():
    return "Point sets"

def const_ContainerPolylines():
    return "Polyline sets"

def const_ContainerPolygons():
    return "Polygon sets"

def const_keyPrestackObject_AMAS():
    return "PrestackObject"

def const_keyVelocityVolume_AMAS():
    return "VelocityVolume"

def const_keyAngle_AMAS():
    return "Angle"

def const_keyILViz_AMAS():
    return "ILViz"

def const_keyILLocation_AMAS():
    return "ILLocation"

def const_keyXLLocation_AMAS():
    return "XLLocation"

def const_AngleMuteAndStacksName():
    return "Angle mute and stacks"

def const_strWorkflowsContainer():
    return "Workflows"

def const_keyTraceHeaderMathInline():
    return "TraceHeaderMathInline"

def const_keyTraceHeaderMathCrossline():
    return "TraceHeaderMathCrossline"

def const_keyTraceHeaderMathEasting():
    return "TraceHeaderMathEasting"

def const_keyTraceHeaderMathNorthing():
    return "TraceHeaderMathNorthing"

def const_keyTraceHeaderMathOffset():
    return "TraceHeaderMathOffset"

def const_keyTraceHeaderMathAzimuth():
    return "TraceHeaderMathAzimuth"

def const_menuCopyLattice():
    return "Copy lattice"

def const_cursorReadoutFromCenter():
    return "Center"

def const_cursorReadoutFromLeft():
    return "Left"

def const_cursorReadoutFromRight():
    return "Right"

def const_keyConstraintRegion():
    return "ConstraintRegion"

def const_keyInterpolationMode():
    return "InterpolationMode"

def const_keyPrestackObject():
    return "PrestackObject"

def const_strPointset():
    return "Pointset"

def const_strTriangleSurface():
    return "Triangle surface"

def const_keySizeDim0():
    return "SizeDim0"

def const_keySizeDim1():
    return "SizeDim1"

def const_keySizeDim2():
    return "SizeDim2"

def const_buttonPauseCaching():
    return "{name?='*Object.Prefetch.CustomButtonWidget.0*' type='omui::CustomButtonWidget_c' visible='1'}"

def const_keyCreateNewTraceHeaders():
    return "CreateNewTraceHeaders"

def const_typeSEGY():
    return "SEGY"

def const_typeZGY():
    return "ZGY"

def const_typeGoCAD():
    return "GoCAD"

def const_algCoRenderInlineSlice():
    return "CreateCoRenderInstanceInlineSlice"

def const_algCoRenderThreeWayInlineSlice():
    return "CreateCoRenderThreeWayInstanceInlineSlice"

def const_menuWellLogColor(intNo):
    intNo = intNo - 1 # starts at 0
    return "WellLogColor%d" % intNo

def const_menuWellLogDisplacement(intNo):
    intNo = intNo - 1 # starts at 0
    return "WellLogDisplacement%d" % intNo

def const_menuWellLogColorTableTemplate(intNo):
    intNo = intNo - 1 # starts at 0
    return "TransferFunction1D%d" % intNo

def const_menuDisplayModeWellLog():
    return "ActiveWellLogDisplayMode"

def const_type3DPrestack():
    return "3DPrestack"

def const_type3DPoststack():
    return "3DPoststack"

def const_type2DGather():
    return "2DGather"

def const_type2DStack():
    return "2DStack"

def const_typeHorizon():
    return "Horizon"

def const_typeVerticalFunctions():
    return "VerticalFunctions"

def const_typeWellHead():
    return "WellHead"

def const_typeWellPath():
    return "WellPath"

def const_typeWellCheckshot():
    return "WellCheckshot"

def const_typeWellMarker():
    return "WellMarker"

def const_typeWellLog():
    return "WellLog"

def const_horizonAttributePos():
    return "HorizonAttributePos"

def const_datasetHoover():
    return "Hoover"

def const_datasetEMV():
    return "EMVision"

def const_datasetWintershall():
    return "Wintershall"

def const_datasetTera():
    return "Tera"

def const_datasetLundin():
    return "Lundin"

def const_datasetSynthetic():
    return "Synthetic"

def const_datasetPICEANCE():
    return "PICEANCE"

def const_datasetAustralian():
    return "Australian"

def const_datasetNovaScotia():
    return "Nova_Scotia"

def const_datasetPolarcus():
    return "Polarcus"

def const_datasetGeoprocesados():
    return "Geoprocesados"


#====test====
def const_keyParentLevel():
    return "ParentLevel"

def const_keyObjectIndex():
    return "ObjectIndex"

def const_relationSibling():
    return "Sibling"

def const_relationChild():
    return "Child"

def const_relationParent():
    return "Parent"

def const_propText():
    return "text"

def const_propDisplayText():
    return "displayText"

def const_propToolTip():
    return "toolTip"

def const_propWidth():
    return "width"

def const_propHeight():
    return "height"

def const_propObjectName():
    return "objectName"

def const_propVisible():
    return "visible"

def const_propX():
    return "x"

def const_propY():
    return "y"

def const_propID():
    return "id"

def const_propType():
    return "type"

def const_parseInfoNumberx2():
    return "parseInfoNumberx2"

def const_parseInfoNumber():
    return "parseInfoNumber"

def const_parseInfoNumberx3():
    return "parseInfoNumberx3"

def const_parseInfoNumberLineEdit():
    return "parseInfoNumberLineEdit" 
               
def const_parseInfoTextLineEdit():
    return "parseInfoTextLineEdit" 
               
def const_parseInfoFilenameLineEdit():
    return "parseInfoFilenameLineEdit" 

def const_parseInfoBoolButton():
    return "parseInfoBoolButton"
     
def const_parseInfoEnumButton():
    return "parseInfoEnumButton"
     
def const_parseInfoFilenameButton():
    return "parseInfoFilenameButton"

def const_parseInfoColorButton():
    return "parseInfoColorButton"
     
def const_parseInfoReferenceCombobox():
    return "parseInfoReferenceCombobox"
     
def const_parseInfoEnumCombobox():
    return "parseInfoEnumCombobox"

#====test====
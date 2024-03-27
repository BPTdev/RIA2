<?php

namespace App\Helpers;

class ConversionHelper
{
    public static function convertToJsonForUi($json)
    {
        $temp = [];
        $data = json_decode($json, true);
        foreach ($data['Labels'] as $label) {
            $temp[] = [
                'name' => $label['Name'],
                'confidence' => $label['Confidence'],
            ];
        }
        return $temp;
    }
}
